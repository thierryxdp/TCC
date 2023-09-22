def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    splited_phrase = frases
    for sinal in sinais:
    	splited_phrase = splited_phrase.rsplit(sinal)

    return len(splited_phrase)