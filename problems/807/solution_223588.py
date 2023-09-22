def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    i = 0
    for sinal in sinais:
    	splited_phrase = frases.count(sinais[i])
        i += 1

	return splited_phrase