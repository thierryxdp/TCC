import re
def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']

	return re.split('; |, |\*|\n', frases)