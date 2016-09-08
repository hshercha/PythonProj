import unittest


import env

from source.Manager import Customer

class CustomerTest( unittest.TestCase ):
    
    # preparing to test
    def setUp( self ):
        print "CustomerTest:setUp-Begin"
        self.customer = Customer()
        print "CustomerTest:setUp-End"
     
    # ending the test
    def tearDown( self ):
        print "CustomerTest:tearDown-Begin"
        del self.customer
        print "CustomerTest:tearDown-End"
     
    # test setName
    def testSetName( self ):
        print ( "START: testSetName" )
        
        with self.assertRaises( ValueError ):
            self.customer.setName( None )
        
        self.customer.setName( "James Brown" )
        self.assertEqual( self.customer.name, "James Brown", "Name wasn't set properly." )
        
        self.customer.setName( "Michael Jackson" )
        self.assertEqual( self.customer.name, "Michael Jackson", "Name wasn't set properly." )
        
        self.customer.setName( "Paul McCartney" )
        self.assertEqual( self.customer.name, "Paul McCartney", "Name wasn't set properly." )
        
        
        print ( "SUCCESS: testSetName" )
    
    # test setLocation
    def testGetRadiansFromDeg( self ):
        print ( "START: testSetLocation" )
            
        with self.assertRaises( ValueError ):
            self.customer.setLocation( None, 12.235 )
        
        with self.assertRaises( ValueError ):
            self.customer.setLocation( 12.235, None )
        
        self.customer.setLocation( 12.232323245, 34.12122354545 )
        self.assertAlmostEqual( self.customer.lat, 12.232323245, 7, "Latitude wasn't set properly." )
        self.assertAlmostEqual( self.customer.long, 34.12122354545, 7, "Longitude wasn't set properly." )
        
        self.customer.setLocation( 45.34358923, -12.45766723 )
        self.assertAlmostEqual( self.customer.lat, 45.34358923, 7, "Latitude wasn't set properly." )
        self.assertAlmostEqual( self.customer.long, -12.45766723, 7, "Longitude wasn't set properly." )
        
        self.customer.setLocation( 51.0201212, -16.2311135 )
        self.assertAlmostEqual( self.customer.lat, 51.0201212, 7, "Latitude wasn't set properly." )
        self.assertAlmostEqual( self.customer.long, -16.2311135, 7, "Longitude wasn't set properly." )
        
        print ( "SUCCESS: testSetLocation" )    
        
if __name__ == '__main__':
    unittest.main()