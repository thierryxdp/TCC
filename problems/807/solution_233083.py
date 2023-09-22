def conta_frases(x):
    a=str.count(x,'.')+str.count(x,'! ')+str.count(x,'? ')-2*str.count(x,'...')
    return a