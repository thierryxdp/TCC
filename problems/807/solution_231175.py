def conta_frases(x):
    ponto = str.count(x,'.')
    exc = str.count(x,'!')
    interrog = str.count(x,'?')
    x = int(ponto + exc +  interrog)
    return x