def conta_frases(t):
    return str.count(t,'.')+str.count(t,'!')+str.count(t,'?')-2*str.count(t,'...')