def conta_frases(frases):
    '''funcao que conta frases tem'''
    sinais = ['.', '!', '?', '...']
    split_frases = frases.count(sinais[0])
    return split_frases