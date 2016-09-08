import unittest

from test_Sphere import SphereTest
from test_Customer import CustomerTest
from test_Manager import ManagerTest


def main():

    testSuite = unittest.TestSuite()
    testSuite.addTest( unittest.makeSuite( SphereTest ) )
    testSuite.addTest( unittest.makeSuite( CustomerTest ) )
    testSuite.addTest( unittest.makeSuite( ManagerTest ) ) 
    testRunner = unittest.TextTestRunner()
    testRunner.run( testSuite )


if __name__ == "__main__":
    main()