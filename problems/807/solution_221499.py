def conta_frases(x):
    x=x.split('!') or x.split('?') and x.split('...') and x.split('.')   
    return len(x)