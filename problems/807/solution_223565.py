def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']

	splited_phrase = frases.split(sinais)
    
    return len(splited_phrase)