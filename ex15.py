# Imports module
from sys import argv

# Unpacks arguments passed to the CLI
script, filename = argv

# Opens the file passed as an input argument
txt = open(filename)

# Reads the content of the filename to the console
print "Here's your file %r:" % filename
print txt.read()

# Prompts user to input the filename in the console
print "Type the filename again:"
file_again = raw_input("> ")

# Opens the file passed as raw_input prompt
txt_again = open(file_again)

# Reads the content of the filename input through the raw_input prompt
print txt_again.read()