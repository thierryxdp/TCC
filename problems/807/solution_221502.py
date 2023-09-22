def conta_frases(x):
    x=x.split('!') and x.split('?') and x.split('...') or x.split('.')   
    return len(x)