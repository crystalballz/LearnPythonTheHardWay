# The next four lines have variable assignments as well as string formatting 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "dont't"
y = "Those who know %s and those who %s." % (binary, do_not)

# These two lines print the aforementioned variables
print x
print y

# These lines declare who exclaimed the aforementioned variables
print "I said: %r." % x
print "I also said: '%s'." % y

# Additional variable assignment 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Evaluation of the joke
print joke_evaluation % hilarious

# Variable assignment to see how concatenating occurs with strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenating the variables assigned directly above
print w + e
