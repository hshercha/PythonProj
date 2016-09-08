import math

def func():
	print "Hi. This program gives the highest prime factor for a given number."
	num = raw_input("Enter a number greater than 1: ")
	num = int(num)
	
	half = int(num/2)
	findPrimeUpto(num, half)

"Based on the Seive of Eratosthenes	
def findPrimeUpto(input, num):
	"Generate a list of numbers from 0 the half
	prime = range(0, num+1)
	
	"0 and 1 are not prime numbers so they are erased from the prime list
	prime[0]= 0
	prime[1]= 0
	
	i = 2
	while (i <= num):
		
		j= math.pow(i, 2)
		j= int(j)
		while(j <= num):
			prime[j] = 0
			j = j+ i;
			
		i = i + 1
		while(i <=num and prime[i]==0 ):
			i = i + 1
	prime = filter(lambda x: x != 0, prime)
	
	print (prime)
	
	print(factors)
	

if __name__ == "__main__":
	func()