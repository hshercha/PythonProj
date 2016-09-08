import json
import random
import time
import math
import argparse
import datetime

'''
usage: createRandomJsonFile.py [-h] events

positional arguments:
  events      Enter numbers of events that you would prefer to generate

optional arguments:
  -h, --help  show this help message and exit
'''

EVENT_KEY_CANCELLED = 'cancelled'
EVENT_KEY_OCCASION = 'occasion'
EVENT_KEY_INVITED_CNT = "invited_count"
EVENT_KEY_YEAR = "year"
EVENT_KEY_MONTH = "month"
EVENT_KEY_DAY = "day"

EVENT_OCCASIONS = [ "Office Party", "Conference", "Movie Night", "SF Marathon", 
                    "Soccer Game", "NBA Game", "Music Concert", "Going away", "Secret flash mob" ]
          
START_DATE = datetime.datetime( 2016, 1, 1 ).toordinal()
END_DATE = datetime.datetime( 2020, 1, 1 ).toordinal()  

DATE_RANGE = END_DATE - START_DATE
        
def main( numOfEvents ):
    data = {}
    data[ 'events' ] = []
    
    for i in range( numOfEvents ):
        event = {}
        event[ EVENT_KEY_OCCASION ] = random.choice( EVENT_OCCASIONS )
        event[ EVENT_KEY_INVITED_CNT ] = random.randint( 0, 100 )
        randomEventDay = random.randint( 0, DATE_RANGE )
        
        randomDateTime = datetime.datetime.fromordinal( START_DATE + randomEventDay )
        event[ EVENT_KEY_YEAR ] = randomDateTime.year
        event[ EVENT_KEY_MONTH ] = randomDateTime.month
        event[ EVENT_KEY_DAY ] = randomDateTime.day
        
        data[ 'events' ].append( event )

    fileName = 'randomEvents_' + str( int( time.time() ) ) + ".txt"
    
    try:
        with open( fileName, 'w' ) as outfile:
            json.dump( data, outfile )
    
    except IOError as err:
        print ( err )
    
    except ValueError as err:
        print ( err )
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "events", help="Enter numbers of events that you would prefer to generate", type=int )
    args = parser.parse_args()
    main( args.events )