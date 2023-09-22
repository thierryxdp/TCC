def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    i = ['!', '.', '?', '...']
    aux = frases.split()
    return len(aux)