import json
import math
import time
import datetime
import calendar

#CONSTANTS
JSON_EVENT_KEY_COUNT = 5

EVENT_KEY_CANCELLED = 'cancelled'
EVENT_KEY_OCCASION = 'occasion'
EVENT_KEY_INVITED_CNT = "invited_count"
EVENT_KEY_YEAR = "year"
EVENT_KEY_MONTH = "month"
EVENT_KEY_DAY = "day"


SET_WIDTH = 7
DASH_AMNT = 55

UNFLAGGED = 0
FLAGGED = 1

UNIX_EPOCH = datetime.datetime( 1970, 1, 1 )

class EventCalendar:
    '''
    EventCalendar class will handle displaying the calendar information
    '''
    
    #Prints the calendar of a particular month that has the events
    #Uses setwidth and hardcoded spaces to display the calendar appropriately
    def printEventMonthCalendar( self, year, month, daysFlaggedForEvents ):
        print '-' * DASH_AMNT
        print( "" )
        print( "  " + calendar.month_abbr[ month ] + "  " + str( year ) ) 
        print( "" )
        print( calendar.weekheader( SET_WIDTH ) )
    
        monthMatrix = calendar.monthcalendar( year, month )
    
        for i in range( 0, len( monthMatrix ) ):
            check = ""
            for j in range( 0, len( monthMatrix[ i ] ) ):
                dayNum = monthMatrix[ i ][ j ]
            
                if dayNum in daysFlaggedForEvents:
                    if ( daysFlaggedForEvents[ dayNum ] == FLAGGED ):
                            
                            #Unflag the day numbers such that day numbers don't mistakenly get
                            # emphasized for other months
                            daysFlaggedForEvents[ dayNum ] = UNFLAGGED
                            check = check + '{0: <8}'.format( self.formatDayNumToStrWithEmphasis( dayNum ) )
                    else:
                        check = check + '{0: <8}'.format( self.formatDayNumToStrNormally( dayNum ) )
                else:
                    check = check + '{0: <8}'.format( self.formatDayNumToStrNormally( dayNum ) )
        
            print check
        print( "" )
	
	#Formats the day number to show emphasis if it was flagged
    def formatDayNumToStrWithEmphasis( self, day ):
        dayStr = ""
        if day >= 10:
            dayStr = '[ ' + str( day ) + ' ]'
        else:
            if day == 0:
                dayStr = '[    ]'
            else:
                dayStr = '[ 0' + str( day ) + ' ]'
    
        return dayStr
    
    #Formats the day number normally since it was not flagged
    def formatDayNumToStrNormally( self, day ):
        dayStr = ""
    
        if day >= 10:
            dayStr = '  ' + str( day ) + '  '
        else:
            if day == 0:
                dayStr = '      '
            else:
                dayStr = '  0' + str( day ) + '  '
    
        return dayStr

class Event:
    '''
    Event class is the model for the event information.
    Stores the occasion and invited count
    '''
    
    #Initialize member variables
    def __init__( self ):
        self.occasion = ""
        self.invitedCount = 0
        self.eventStatus = True
        self.eventDay = 0
    
    def setOccasion( self, occasion ):
        if occasion is None:
            raise ValueError( "Occassion is invalid" )
        self.occasion = occasion
    
    def setInvitedCount( self, count ):
        if count is None:
            raise ValueError( "Invited Count is invalid" )
        self.invitedCount = count
    
    def cancelEvent( self ):
        self.eventStatus = False   
    
    def setEventDay( self, day ):
        if ( day is None ) or ( day < 1 ):
            raise ValueError( "Event day is invalid" )
        self.eventDay = day

class Manager:
    '''
    Manager class behaves as a facade between the
    Events and the Event Calendar class.
    '''
    
    #Initialize member variables
    def __init__( self ):
        #Dictionary to hold the event objects
        self.events = {}
    
    #Validates each json key and their corresponding value
    def validateEventKeysAndValues( self, event ):
        keyCount = 0
        for key in event:               
            if ( key == EVENT_KEY_OCCASION ):
                if not isinstance( event[ key ], unicode ):
                    raise ValueError( "Expected key-vale as unicode" )
            elif ( key == EVENT_KEY_INVITED_CNT 
                or key == EVENT_KEY_YEAR 
                or key == EVENT_KEY_MONTH 
                or key == EVENT_KEY_DAY ):
                if not isinstance( event[ key ], int ):
                    raise ValueError( "Expected key-value as integer" )
            elif ( key == EVENT_KEY_CANCELLED ):
                if not isinstance( event[ key ], bool ):
                    raise ValueError( "Expected key-value as boolean" )
            else:
                raise ValueError( "Incorrect Event Key" )
                   
            keyCount +=1
        
        if ( keyCount < JSON_EVENT_KEY_COUNT ):
            raise ValueError( "Missing dictionary keys" )
                
    #Validates calendar dates
    def validateCalendarDate( self, year, month, day ):
        try:
            newDate = datetime.datetime( year, month, day )
        except ValueError as err:
            raise ValueError( err )
    
    #Parses the file based on the filename
    def parseFile( self, filename ):
        data = {}
        try:
            with open( filename ) as jsonFile:    
                data = json.load( jsonFile )
            
            eventsList = data[ 'events' ]
            
            for eachEvent in eventsList:
                #Validate all the json keys and their corresponding values
                self.validateEventKeysAndValues( eachEvent )
                
                #Validate all the dates
                self.validateCalendarDate( eachEvent[ EVENT_KEY_YEAR ], eachEvent[ EVENT_KEY_MONTH ], eachEvent[ EVENT_KEY_DAY ] )
                
                #Instantiate the event object
                event = Event()
                event.setOccasion( eachEvent[ EVENT_KEY_OCCASION ] )
                event.setInvitedCount( eachEvent[ EVENT_KEY_INVITED_CNT ] )
                
                #Cancel the event if there is cancel key in the json
                if EVENT_KEY_CANCELLED in eachEvent:
                    event.cancelEvent()
                
                year = eachEvent[ EVENT_KEY_YEAR ]
                month = eachEvent[ EVENT_KEY_MONTH ]
                day = eachEvent[ EVENT_KEY_DAY ]
                
                event.setEventDay( day )
                
                #Using the difference in months between the UNIX epoch and the given date
                #as a key for the dictionary
                monthDiff = (year - UNIX_EPOCH.year)*12 + month - UNIX_EPOCH.month
                
                if monthDiff in self.events:
                    self.events[ monthDiff ].append( event )
                else:
                    savedEvents = []
                    savedEvents.append( event )
                    self.events[ monthDiff ] = savedEvents
                    
        except IOError as err:
            raise IOError( err )
        except ValueError as err:
            raise ValueError( err )
    
    #Print event related information
    def printEventCalendar( self ):
        eventCalendar = EventCalendar()
        curMonth = 0
        curYear = 0
        
        #flagEventDaysInTheMonth flags the actual day numbers (1-31) 
        #in the month that contain the events
        flagEventDaysInMonth = {} 
        
        #mapEventDaysToEventInfo maps the actual days numbers (1-31)
        #in the month to the eventInformation
        mapEventDaysToEventInfo = {}
        
        monthDiffKeys = self.events.keys()
        
        #Sort the keys so the months are displayed in a chronological order
        monthDiffKeys.sort()
        
        #The difference in months between the given time and the UNIX Epoch
        # was used as keys for self.events[]. Use the reverse logic to retrieve the actual month, year 
        for monthDiff in monthDiffKeys:
            givenYear = UNIX_EPOCH.year + ( monthDiff / 12 )
            givenMonth = UNIX_EPOCH.month + ( monthDiff % 12 )
            
            #If the current month or year changes, display the current calendar with
            # the events associated to it and update the month and year
            if ( givenYear != curYear or givenMonth != curMonth ):
                
                #Ensure that there is event related information available for that month
                if len( mapEventDaysToEventInfo ) > 0:
                    eventCalendar.printEventMonthCalendar( curYear, curMonth, flagEventDaysInMonth )
                    self.printEventInfoList( mapEventDaysToEventInfo )
                    del mapEventDaysToEventInfo
                    mapEventDaysToEventInfo = {}
                curYear = givenYear
                curMonth = givenMonth
            
            #Retrieve all the event list for that month
            eventList = self.events[ monthDiff ]
            
            for eachEvent in eventList:
                eventDay = eachEvent.eventDay
                
                #Flag the day of the month so the calendar display function can show
                flagEventDaysInMonth[ eventDay ] = FLAGGED
            
            
                if eventDay in mapEventDaysToEventInfo:
                    mapEventDaysToEventInfo[ eventDay ].append( eachEvent )
                else:
                    mapEventDaysToEventInfo[ eventDay ] = []
                    mapEventDaysToEventInfo[ eventDay ].append( eachEvent )
        
        eventCalendar.printEventMonthCalendar( curYear, curMonth, flagEventDaysInMonth )
        self.printEventInfoList( mapEventDaysToEventInfo )
        print '-' * DASH_AMNT
    
    #Print event list
    def printEventInfoList( self, daysMappedToEventInfo ):
        curDay = 0
        
        dayKeys = daysMappedToEventInfo.keys()
        
        print( "[ Events ]")
        #Sort the keys so that events are displayed in a chronological order
        dayKeys.sort()
        for day in dayKeys:
            if ( day != curDay ):
                curDay = day
                print '-' * DASH_AMNT
                
                if day < 10:
                    print ( '0' + str( day ) + "|" )
                else:
                    print( str( day ) + "|" )
                print '-' * DASH_AMNT
            
            #There could be multiple events on a day
            #Pop the list till there are not events left for the day
            while( len( daysMappedToEventInfo[ day ] ) > 0 ):
                event = daysMappedToEventInfo[ day ].pop()
                eventOccassion = "->| " + event.occasion 
                print eventOccassion
                eventSummary = "   ** Invited: " + str(event.invitedCount) + ", Status: "
            
                if event.eventStatus:
                    eventSummary = eventSummary + "Ongoing"
                else:
                    eventSummary = eventSummary + "Cancelled"
            
                print eventSummary
        
                