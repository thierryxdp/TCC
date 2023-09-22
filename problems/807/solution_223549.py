def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    for sinal in sinais:
    frases=frases.split(sinais)
    return len(frases)