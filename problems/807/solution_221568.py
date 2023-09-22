def conta_frases(x):
    y=x.split('.') and x.split('!') and x.split('?') and x.split('...')   
    return len(y)