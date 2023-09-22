import re

def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    
	x = (re.split('[.!?]', frases))
    
    return len(x)