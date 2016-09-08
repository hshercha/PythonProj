def func():
	nums = range(1, 1000)
		
	nums = filter(lambda x: x % 3 == 0 or x % 5 == 0, nums)
	
	print sum(nums)

if __name__ == "__main__":
	func()