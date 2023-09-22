def conta_frases(x):
    return str.count(x,'.')+str.count(x,'!')+str.count(x,'?')-2*str.count(x,'...')