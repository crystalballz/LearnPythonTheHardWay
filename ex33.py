def count_from_zero(end,increments):

	i = 0
	numbers = []
	
	while i < end:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += increments
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
		
	print "The numbers: "

	for num in numbers:
		print num
		
		
count_from_zero(10,2)