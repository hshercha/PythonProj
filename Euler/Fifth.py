import math

def gcd(a,b):
	if b == 0:
		return a
	elif a == 0:
		return b
	else:
		if a >= b:
			remain = a % b
			return gcd(b, remain)
		else:
			remain = b % a
			return gcd(a, remain)

def lcm(a,b):
	return ((a * b) / gcd(a * b))

if __name__ == "__main__":
	func()
