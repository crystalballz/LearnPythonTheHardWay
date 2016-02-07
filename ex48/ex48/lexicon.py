direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verb = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
noun = ['door', 'bear', 'princes', 'cabinet']
number = [i for i in range(10)]


	
def scan(sentence):
	words = sentence.split()
	new_sentence = []
	for word in words:
		# determine if it is a direction	
		if word in direction:
			 word = ('direction', '%s' % word)
		
		# determine if it is a verb	
		elif word in verb:
			 word = ('verb', '%s' % word)	 
		
		# determine if it is a stop	
		elif word in stop:
			 word = ('stop', '%s' % word)	 
		
		# determine if it is a noun	
		elif word in noun:
			 word = ('noun', '%s' % word)	 
		
		# determine if it is a number	
		elif word in number:
			 word = ('number', convert_number(word))	 
		
		# determine if the word is error
		else:
			word = ('error', '%s' % word)
		
		new_sentence.append(word)
	return new_sentence
		
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
		
	