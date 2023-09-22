def conta_frases(x):
    x=x.split('!') or x.split('?') or x.split('...') or x.split('.')   
    return len(x)