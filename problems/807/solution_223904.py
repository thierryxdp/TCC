def conta_frases (frases):
    '''funcao que conta quantas frases tem'''
    sinais = ['.', '!', '?', '...']
    split_frases = frases.count(sinais[0])
    return len(split_frases)