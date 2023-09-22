def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    
    splited = ''
    for sinal in sinais:
        splited = frases.split(sinal)
        
    return len(splited)