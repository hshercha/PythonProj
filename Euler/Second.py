def func():
	nums = []
	nums.append( 1 )
	nums.append( 2 )
	val = nums[0] + nums[1]
	i = 2;
	while (val < 4000000):
		 nums.append(val)
		 val = nums[i] + nums[i - 1]
		 i = i + 1
	print ( val )
	nums = filter(lambda x: x % 2 == 0, nums)
	sum = 0
	sum = reduce(lambda x, y: x + y, nums)	
	print ( sum )


if __name__ == "__main__":
	func()