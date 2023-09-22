def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    
    for sinal in sinais:
    	splited_phrase = frases.count(sinal)

    return splited_phrase