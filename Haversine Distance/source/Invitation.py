import argparse
from Manager import Manager

'''
usage: Invitation.py [-h] filename

positional arguments:
  filename    Enter json file of customers information

optional arguments:
  -h, --help  show this help message and exit

'''

#CONSTANTS
NEARBY_RADIUS = 100
LAT_DEG = 53.3381985
LONG_DEG = -6.2592576

def main( fileName ):
	manager = Manager()
	
	try:
		manager.parseFile( fileName )
		manager.displaysCustomersWithinRadiusAndLocation( NEARBY_RADIUS, LAT_DEG, LONG_DEG )
	except IOError as err:
		print( "Error opening file\n" )
		print( err )
	except ValueError as err:
		print( "Error parsing file\n" )
		print( err )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "filename", help="Enter json file of customers information" )
    args = parser.parse_args()
    main( args.filename )
	