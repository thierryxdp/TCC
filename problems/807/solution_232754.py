def conta_frases (x):
    '''função conta frases do texto'''
    return (str.count(x, '!') + str.count(x, '.') + str.count(x, '?') + str.count(x, '...'))