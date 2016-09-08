import unittest
import math

import env

from source.Manager import Sphere

class SphereTest( unittest.TestCase ):
     
    # preparing to test
    def setUp( self ):
        print "SphereTest:setUp-Begin"
        self.earth = Sphere()
        print "SphereTest:setUp-End"
     
    # ending the test
    def tearDown( self ):
        print "SphereTest:tearDown-Begin"
        del self.earth
        print "SphereTest:tearDown-End"
     
    # test getDistanceBetweenTwoPoints
    def testDistanceBetweenTwoPoints( self ):
        print ( "START: testDistanceBetweenTwoPoints" )
        
        actualDistance = self.earth.getDistanceBetweenPoints( -25.12614, -18.31509, -26.68400, -82.63347, 6471 )
        expectedDistance = 6463
        
        self.assertLessEqual( math.fabs(expectedDistance - actualDistance), 1, "Incorrect calculations on distance." )
        
        actualDistance = self.earth.getDistanceBetweenPoints( -35.12614, 58.31509, -29.68400, 34.2347, 6471 )
        expectedDistance = 2371
        
        self.assertLessEqual( math.fabs(expectedDistance - actualDistance), 1, "Incorrect calculations on distance." )
        
        actualDistance = self.earth.getDistanceBetweenPoints( 15.12614, 38.31509, 45.468400, -92.63347, 6471 )
        expectedDistance = 11851
        
        self.assertLessEqual( math.fabs(expectedDistance - actualDistance), 1, "Incorrect calculations on distance." )
        
        
        print ( "SUCCESS: testDistanceBetweenTwoPoints" )
    
    # test getRadiansFromDeg
    def testGetRadiansFromDeg( self ):
        print ( "START: testGetRadiansFromDeg" )
        
        actualRadians = self.earth.getRadiansFromDeg( 90 )
        expectedRadians = math.pi / 2
        
        self.assertAlmostEqual( actualRadians, expectedRadians, 7, "Incorrect conversion to radians." )
        
        actualRadians = self.earth.getRadiansFromDeg( 180 )
        expectedRadians = math.pi 
        
        self.assertAlmostEqual( actualRadians, expectedRadians, 7, "Incorrect conversion to radians." )
        
        actualRadians = self.earth.getRadiansFromDeg( 0 )
        expectedRadians = 0
        
        self.assertEqual( actualRadians, expectedRadians, "Incorrect converstion to radians." )
        
        print ( "SUCCESS: testGetRadiansFromDeg" )    
        
if __name__ == '__main__':
    unittest.main()