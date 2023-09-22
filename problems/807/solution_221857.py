def conta_frases(x):
    x=x.replace('...','"')
    x=x.replace('!','"')
    x=x.replace('.','"')
    x=x.replace('?','"')
    return len(x)