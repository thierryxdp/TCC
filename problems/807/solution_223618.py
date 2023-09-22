def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais=['.', '!', '?', '...']
    
    splited = ''
    i = 0
    for sinal in sinais:
        splited = frases.split(sinais[i])
        i += 1
        
    return len(splited)