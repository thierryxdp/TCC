def conta_frases(x):
    y=x.split('.')
    y=x.split('!')
    y=x.split('?')
    y=x.split('...')   
    return len(y)