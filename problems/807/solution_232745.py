def conta_frases (x):
    '''função conta frases do texto'''
    (str.count(x, '!') + str.count(x, '.') + str.count(x, '?') + str.count(x, '...'))