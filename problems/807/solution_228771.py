def conta_frases():
    '''função que conta quantas frases tem'''
    sinais=['-', '?', '...']
    
    split_frases = frases.count(sinais[0])
    
    return split_frases