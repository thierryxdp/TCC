def conta_frases(x):
    ponto = str.count(x,'.')
    exc = str.count(x,'!')
    retcs = str.count(x,'...')
    interrog = str.count(x,'?')
    x = int(ponto + exc + retcs + interrog)
    if ponto !=1:
        return ponto==0
    return x