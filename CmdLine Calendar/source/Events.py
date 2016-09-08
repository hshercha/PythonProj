import argparse
import calendar
from Manager import Manager

'''
usage: Invitation.py [-h] filename

positional arguments:
  filename    Enter json file of events information

optional arguments:
  -h, --help  show this help message and exit

sample output:
      Dec  2015

      Mon     Tue     Wed     Thu     Fri     Sat     Sun  
              01      02      03      04      05      06    
      07      08      09      10      11      12      13    
      14      15      16    [ 17 ]    18      19      20    
      21      22      23      24      25      26      27    
      28      29      30      31                            

    [ Events ]
    -------------------------------------------------------
    17|
    -------------------------------------------------------
    ->| Press release
       ** Invited: 64, Status: Cancelled
    -------------------------------------------------------

      Jan  2016

      Mon     Tue     Wed     Thu     Fri     Sat     Sun  
                                    [ 01 ]    02      03    
      04      05      06      07      08      09      10    
      11      12      13      14      15      16      17    
      18      19      20      21      22      23    [ 24 ]  
      25      26      27      28      29      30      31    

    [ Events ]
    -------------------------------------------------------
    01|
    -------------------------------------------------------
    ->| Going away party
       ** Invited: 21, Status: Ongoing
    ->| New year party
       ** Invited: 55, Status: Ongoing
    -------------------------------------------------------
    24|
    -------------------------------------------------------
    ->| Graduation Party
       ** Invited: 55, Status: Ongoing
    -------------------------------------------------------

      Feb  2016

      Mon     Tue     Wed     Thu     Fri     Sat     Sun  
      01      02      03      04      05      06      07    
      08      09      10      11      12      13    [ 14 ]  
      15      16      17      18      19      20      21    
      22      23      24      25      26      27      28    
      29                                                    

    [ Events ]
    -------------------------------------------------------
    14|
    -------------------------------------------------------
    ->| Birthday party
       ** Invited: 120, Status: Ongoing
    -------------------------------------------------------

      Nov  2016

      Mon     Tue     Wed     Thu     Fri     Sat     Sun  
              01      02      03      04      05      06    
      07      08      09      10      11      12      13    
      14      15      16      17      18      19      20    
      21      22      23    [ 24 ]    25      26      27    
      28      29      30                                    

    [ Events ]
    -------------------------------------------------------
    24|
    -------------------------------------------------------
    ->| Technical discussion
       ** Invited: 23, Status: Ongoing
    -------------------------------------------------------

'''

def main( fileName ):
	manager = Manager()
    
	try:
		manager.parseFile( fileName )
		manager.printEventCalendar()
	except IOError as err:
		print( "Error opening file\n" )
		print( err )
	except ValueError as err:
		print( "Error parsing file\n" )
		print( err )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "filename", help="Enter json file of events information" )
    args = parser.parse_args()
    main( args.filename )
	