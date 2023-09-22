def conta_frases(x):
    a=str.count(x,'. ')+str.count(x,'! ')+str.count(x,'? ')+str.count(x,'...')
    return a+1