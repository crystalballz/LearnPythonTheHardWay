from nose.tools import *
from ex49 import parser

def test_Sentence():
	s = parser.Sentence(('noun', 'princess'), ('verb', 'open'), ('noun', 'door'))
	assert_equal(s.subject, 'princess')
	assert_equal(s.verb, 'open')
	assert_equal(s.object, 'door')

def test_peek():
	word_list = [('noun', 'bear')]
	assert_equal(peek(word_list), 'noun')
	assert_equal(peek(None), None)
	
	
def test_match():
	word_list = [('noun', 'player')]
	assert_equal(parser.match(word_list, 'noun'), 'player')
	assert_equal(parser.match(None, 'noun'), None)


def test_skip():
	pass
						  
def test_parse_verb():
	pass

def test_parse_object():
	pass
						  
def test_parse_subject():
	pass
						  
def test_parse_sentence():
	pass

def test_parserError():
	pass