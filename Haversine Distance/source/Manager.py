import json
import math

#CONSTANTS
EARTH_RADIUS = 6371

class Sphere:
	'''
    Sphere class is used to perform any calculations pertaining to a sphere.
    '''
    
	#Converts degrees to radians
	def getRadiansFromDeg( self, deg ):
		rad = deg * (math.pi/180)
		return rad
	
	#Gets distance between two points on the sphere using the Haversine formula
	def getDistanceBetweenPoints( self, degLat1, degLong1, degLat2, degLong2, sphereRadius ):
	
		#Uses the Haversine formula to calculate the distance
		#   a = Math.sin(delta_phi/2) * Math.sin(delta_phi/2) +
		#       Math.cos(phi1) * Math.cos(phi2) *
		#       Math.sin(delta_lambda/2) * Math.sin(delta_lambda/2)
	    #
		#	where phi1 and phi2 are latitude values in radians
		#	where delta_phi is the difference of the latitude values in radians
		#	where delta_lambda is the difference of the longitude values in radians 
		# 	
		#	arcAngle = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
		#   arcLength = EARTH_RADIUS * arcAngle
    
		degLatDiff = degLat2 - degLat1
		degLongDiff = degLong2 - degLong1
		
		latOneRadians = self.getRadiansFromDeg( degLat1 )
		latTwoRadians = self.getRadiansFromDeg( degLat2 )
		latDiffRadians = self.getRadiansFromDeg( degLatDiff )
		longDiffRadians = self.getRadiansFromDeg( degLongDiff )
		
		a = ( math.sin( latDiffRadians/2 ) * math.sin( latDiffRadians/2 ) 
			+ ( math.cos( latOneRadians ) * math.cos( latTwoRadians )
			*   math.sin( longDiffRadians/2 ) * math.sin( longDiffRadians/2 ) ) )
		
		arcAngle = 2 * math.atan2( math.sqrt( a ), math.sqrt( 1 - a ) )
		
		length = sphereRadius * arcAngle
		
		return length

class Customer:
    '''
    Customer class is the model for the customer information.
    '''
    
	#Initialize member variables
    def __init__( self ):
		self.name = ""
		self.lat = 0.0
		self.long = 0.0
    
    #Sets the name of the customer
    def setName( self, name ):
		if name is None:
			raise ValueError( "Empty Name" )
		else:
			self.name = name
	
    def setLocation( self, lat, long ):
		if lat is None:
			raise ValueError( "Empty Latitude" )
		else:
			self.lat = lat
		
		if long is None:
			raise ValueError( "Empty Longitude" )
		else:
			self.long = long

class Manager:
    '''
    Manager class behaves as a facade between the
    Invitation and the Customer and the Sphere class.
    '''
    
	#Initialize member variables
    def __init__( self ):
		self.customers = {}

	#Parses the file based on the filename
    def parseFile( self, filename ):
		try:
			with open( filename ) as fp:
				for line in fp:
					self.parseJsonString( line )
		except ValueError as err:
			raise ValueError( err )
		except IOError as err:
			raise IOError( err )

	#Parses each JSON line in the file
    def parseJsonString( self, jsonLine ):
		try:
			parsedObject = json.loads( jsonLine )
		except ValueError as err:
			raise ValueError( err )
		
		userID = parsedObject[ 'user_id' ]
		name = parsedObject[ 'name' ]
		latitude = parsedObject[ 'latitude' ]
		longitude = parsedObject[ 'longitude' ]
		
		self.validateJsonValues( userID, name, latitude, longitude )
		
		customer = Customer()
		customer.setName( name )
		customer.setLocation( float( latitude ), float ( longitude ) )
		
		if userID in self.customers:
			raise ValueError( "Duplicate values" )
		else:
			self.customers[ userID ] = customer
	
	#Validates the parsed json values
    def validateJsonValues( self, userID, name, latitude, longitude ):
		if not isinstance( userID, int ):
			raise ValueError( "Expected user id as integer" )

		if userID < 0:
			raise ValueError( "Expected whole number as user_id'" )
		
		if not isinstance( name, unicode ):
			raise ValueError( "Expected name as unicode" )
		
		if not isinstance( latitude, unicode ):
			raise ValueError( "Expected latitude as unicode" )
		
		if not isinstance( longitude, unicode ):
			raise ValueError( "Expected longitude as unicode" )
		
		try:
			lat = float( latitude )
		except ValueError as err:
			raise ValueError(err)
		
		try:
			long = float( longitude )
		except ValueError as err:
			raise ValueError( err )
	
	#Returns the customer name based on their userID
    def getCustomerName( self, userID ):
		if userID in self.customers:
			return self.customers[ userID ].name
		else:
			return None
	
	#Returns the customer location based on their userID
    def getCustomerLocation( self, userID ):
		if userID in self.customers:
			return ( self.customers[ userID ].lat, self.customers[ userID ].long )
		else:
			return None
		 
	#Prints a list of customers within the radius of the provided coordinates
    def displaysCustomersWithinRadiusAndLocation( self, radius, latDeg, longDeg ):
		validCustomers = self.findCustomersWithinRadiusAndLocation( radius, latDeg, longDeg)
		
		if len( validCustomers ) == 0:
			print "Unfortunately, there are not customers who lives within the radius of " + str( radius )
		
		#Sort the id list in ascending order
		
		validCustomers.sort()
		for customerID in validCustomers:
			print str( customerID ) + ", " + self.customers[ customerID ].name
		
	#Returns a list of customerIDs within the radius of the provided coordinates
    def findCustomersWithinRadiusAndLocation( self, radius, latDeg, longDeg ):
		earth = Sphere()
		
		validCustomers = []
		if self.customers is None:
			return None
		
		for id in self.customers:
			distance = earth.getDistanceBetweenPoints( self.customers[ id ].lat, self.customers[ id ].long, latDeg, longDeg, EARTH_RADIUS )
			
			if ( distance <= radius ):
				
				validCustomers.append( id )
		
		return validCustomers	
	
	
	
		
		
		
		
		
	