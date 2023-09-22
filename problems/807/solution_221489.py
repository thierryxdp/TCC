def conta_frases(x):
    x=x.split('!')   
    x=x.split('.')
    x=x.split('...')
    x=x.split('?')
    return len(x)