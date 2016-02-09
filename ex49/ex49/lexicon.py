direction = ['north', 'south', 'east', 'west', 'down', 'up', 
			 'left', 'right', 'back', 'forward', 'under']
verb = ['go', 'stop', 'kill', 'eat', 'run', 'hide', 'open', 'close']
stop = ['the', 'in', 'of', 'from', 'at', 'it', 'a', 'an', 'is']
noun = ['door', 'bear', 'princess', 'cabinet', 'tree', 'bush']


	
def scan(sentence):
	words = sentence.split()
	new_sentence = []
	for word in words:
		x = word.lower()
		# determine if word is a direction	
		if x in direction:
			 word = ('direction', '%s' % x)
		
		# determine if word is a verb	
		elif x in verb:
			 word = ('verb', '%s' % x)	 
		
		# determine if word is a stop	
		elif x in stop:
			 word = ('stop', '%s' % x)	 
		
		# determine if word is a noun	
		elif x in noun:
			 word = ('noun', '%s' % x)	 
		
		# determine if word is a number	
		elif word.isdigit():
			 word = ('number', convert_number(word))	 
		
		# determine if word is error
		else:
			word = ('error', '%s' % word)
		
		# adds word tuple to new_sentence
		new_sentence.append(word)
	
	return new_sentence
		
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
		
	