import unittest

import env

from source.Manager import Manager

class ManagerTest( unittest.TestCase ):
     
    # preparing to test
    def setUp( self ):
        print "ManagerTest:setUp-Begin"
        self.manager = Manager()
        print "ManagerTest:setUp-End"
     
    # ending the test
    def tearDown( self ):
        print "ManagerTest:tearDown-Begin"
        del self.manager
        print "ManagerTest:tearDown-End"
    
    # test parseFile with invalid inputs
    def testParseFileWithInvalidInputs( self ):
        print ( "START: testParseFileWithInvalidInputs" )
        
        with self.assertRaises( IOError ):
            self.manager.parseFile( "random123.txt" )
        
        with self.assertRaises( IOError ):
            self.manager.parseFile( "random231.txt" )
        
        with self.assertRaises( IOError ):
            self.manager.parseFile( "random456.txt" )
        
        print ( "END: testParseFileWithInvalidInputs" )
        
    # test parseJsonString with valid inputs
    def testParseJsonStringWithValidInputs( self ):
        print ( "START: testParseJsonStringWithValidInputs" )
        self.manager.parseJsonString( '{"latitude": "53.74452", "user_id": 21, "name": "Prince", "longitude": "-8.11167"}' )
        
        actualName = self.manager.getCustomerName( 21 )
        expectedName = "Prince"
        actualLat, actualLong = self.manager.getCustomerLocation( 21 )
        expectedLat = 53.74452
        expectedLong = -8.11167
        self.assertNotEqual( actualName, None, "Name wasn't registered." )
        self.assertNotEqual( actualLat, None, "Latitude was't registered." )
        self.assertNotEqual( actualLong, None, "Longitude wasn't registered." )
        
        self.assertEqual( actualName, expectedName, "Names don't match." )
        self.assertAlmostEqual( actualLat, expectedLat, 7, "Latitudes doesn't match." )
        self.assertAlmostEqual( actualLong, expectedLong, 7, "Longitudes doesn't match." )
        
        self.manager.parseJsonString( '{"latitude": "54.0894797", "user_id": 100, "name": "Michael Jackson", "longitude": "-6.18671"}' )
        
        actualName = self.manager.getCustomerName( 100 )
        expectedName = "Michael Jackson"
        actualLat, actualLong = self.manager.getCustomerLocation( 100 )
        expectedLat = 54.0894797
        expectedLong = -6.18671
        self.assertNotEqual( actualName, None, "Name wasn't registered." )
        self.assertNotEqual( actualLat, None, "Latitude was't registered." )
        self.assertNotEqual( actualLong, None, "Longitude wasn't registered." )
        
        self.assertEqual( actualName, expectedName, "Names don't match." )
        self.assertAlmostEqual( actualLat, expectedLat, 7, "Latitudes doesn't match." )
        self.assertAlmostEqual( actualLong, expectedLong, 7, "Longitudes doesn't match." )
        
        self.manager.parseJsonString( '{"latitude": "51.999447", "user_id": 42, "name": "James Brown", "longitude": "-8.11167"}' )
        
        actualName = self.manager.getCustomerName( 42 )
        expectedName = "James Brown"
        actualLat, actualLong = self.manager.getCustomerLocation( 42 )
        expectedLat = 51.999447
        expectedLong = -8.11167
        self.assertNotEqual( actualName, None, "Name wasn't registered." )
        self.assertNotEqual( actualLat, None, "Latitude was't registered." )
        self.assertNotEqual( actualLong, None, "Longitude wasn't registered." )
        
        self.assertEqual( actualName, expectedName, "Names don't match." )
        self.assertAlmostEqual( actualLat, expectedLat, 7, "Latitudes doesn't match." )
        self.assertAlmostEqual( actualLong, expectedLong, 7, "Longitudes doesn't match." )
        
        print ( "SUCCESS: testParseJsonStringWithValidInputs" )
    
        # test parseJsonString with invalid inputs
    def testParseJsonStringWithInvalidInputs( self ):
        print ( "START: testParseJsonStringWithInvalidInputs" )     
        with self.assertRaises( ValueError ):
            self.manager.parseJsonString( '{"latitude": "53.74452", ""-8.11167"}' )
        
        with self.assertRaises( ValueError ):
            self.manager.parseJsonString( 'adfadfadfa' )
        
        try:
            self.manager.parseJsonString( '{"latitude": "53.74452", "user_id": 21, "name": "John Doe", "longitude": "-8.11167"}' )
        except ValueError as err:
            self.fail( err )
        
        #This test case insures against overwriting the same userID
        with self.assertRaises( ValueError ):
            self.manager.parseJsonString( '{"latitude": "53.74452", "user_id": 21, "name": "Prince", "longitude": "-8.11167"}' )
        
        print ( "SUCCESS: testParseJsonStringWithInvalidInputs" )
    
    # test validateJsonValues with valid inputs
    def testValidateJsonValueWithValidInputs( self ):
        print ( "START: testValidateJsonValueWithValidInputs" )
        

        try:
            self.manager.validateJsonValues( 1, u"James Brown", u"57.109", u"-12.12344" )
            self.manager.validateJsonValues( 8, u"John Lennon", u"54.1112", u"-19.5344" )
            self.manager.validateJsonValues( 9, u"Michael Jackson", u"23.109", u"-18.13444" )
            self.manager.validateJsonValues( 10, u"Paul McCartney", u"45.109", u"-17.42344" )
            self.manager.validateJsonValues( 11, u"Steve Austin", u"43.179", u"-11.52344" )
            self.manager.validateJsonValues( 2, u"Hulk Hogan", u"65.179", u"-14.6344" )
            self.manager.validateJsonValues( 45, u"Saun Carter", u"67.709", u"-13.7844" )
            self.manager.validateJsonValues( 17, u"Kanye West", u"45.609", u"-9.12344" )
            self.manager.validateJsonValues( 19, u"James Cameron", u"35.109", u"-12.344" )

        except ValueError as err:
            self.fail( err )
        
        print ( "SUCCESS: testValidateJsonValueWithValidInputs" )

    # test validateJsonValues with valid inputs
    def testValidateJsonValueWithInvalidInputs( self ):
        print ( "START: testValidateJsonValueWithInvalidInputs" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100.01, u"James Brown", u"57.109", u"-12.12344" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( -1, u"James Brown", u"57.109", u"-12.12344" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100, 1234, u"57.109", u"-12.12344" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100, u"James Brown", 123, u"-12.12344" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100, u"James Brown", u"57.109", 123 )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100, u"James Brown", u"kkkkkk", u"-12.12344" )
        
        with self.assertRaises( ValueError ):
            self.manager.validateJsonValues( 100.01, u"James Brown", u"57.109", u"kkkk" )
        
        print ( "SUCCESS: testValidateJsonValueWithInvalidInputs" )
        
if __name__ == '__main__':
    unittest.main()