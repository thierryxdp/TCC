def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    
    splited_phrase = frases.counts(sinais)

    return splited_phrase