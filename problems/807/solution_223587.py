def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    i = len(sinais) - 1
    splited_phrase = frases.count(sinais[i])

	return splited_phrase