import math

def func():
	print ("Hi. This program will give the largest palindrome of the a two 3-digit numbers.")
	
	highest = 997
	lowest  = 100
	palindromes = generatePalindrome(lowest, highest)
	
	findHighestPalindrome(palindromes)

def generatePalindrome(low, high):
	palindromes = []
	
	i = high
	
	while(i >= low):
		temp_hund = i
		temp_hund_thou = i * 1000
		palindrome = temp_hund_thou;
		const = 10
		count = 2
	
		while(count >= 0):
			palindrome = int( palindrome + ((temp_hund % const) * math.pow(const, count)) )
			temp_hund = temp_hund//const
			count = count - 1
		i = i - 1
		palindromes.append(palindrome)
	
	return (palindromes)

def findHighestPalindrome(palindromes):
	answer = 0
	
	test = [997799, 996699]
	for i in range(len(palindromes)):
		palindrome = palindromes[i]
		num = palindrome//100000
		numHalf = num/2
		
		sqrt = math.floor(math.sqrt(palindrome))
		print ("sqrt is :")
		print ( sqrt )
		newNum = sqrt
		sqrtMod = int(sqrt) % 10
		evenSeq = False
		factorFive = False

		if ( num == 5 ):
			factorFive = True
			if( (num - sqrtMod) > 0 ):
				newNum = sqrt - sqrtMod
			else:
				newNum = sqrt - Math.abs(num - sqrtMod)
		
		elif ( num == 2 or num == 4 or num == 6 or num == 8 ):
				#convert num to even
				if(int(sqrt) % 2 != 0):
					newNum = sqrt - 1
				evenSeq = True
		else:
			if( num == 1 or num == 3 or num == 7 or num == 9):
				#convert num to odd
				
				if( (int(sqrt) % 2 == 0) and (sqrtMod != 0)):
					newNum = sqrt - 1
				
				if(int(newNum) % 10 == 5):
					newNum = newNum - 2
		
		found = False
		diff = 0
		
		print ("palindrome is:" )
		print ( palindrome )
		while ( (found == False) and (newNum > 99)):
			if( (palindrome/newNum) > 999):
				#print("quotient is great than 999")
				#print(palindrome/newNum)
				break
			diff = (palindrome/newNum) - (palindrome//newNum)
			 
			print (newNum)
			#print (diff)
			if(diff == 0):
				print("diff is 0")
				found = True
				answer = palindrome
			
			else:
				if (int(newNum) % 10 == 0):
			 		if(factorFive):
			 			newNum = newNum - 5
			 		else:
			 			if(evenSeq):
			 				newNum = newNum - 2
			 			else:
			 				newNum = newNum - 1
			 	elif (int(newNum) % 10 == 5):
			 		if(factorFive):
			 			newNum = newNum - 5
			 		else:
			 			newNum = newNum - 2
			 	else:
			 		newNum = newNum - 2
		
		if (found):
			print (answer)
			break
							 
					
					
			
			
			
		

if __name__ == "__main__":
	func()