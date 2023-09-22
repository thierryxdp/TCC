def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais = ['.', '!', '?', '...']
    split_frases = frases.split(sinais[0])
    return split_frases