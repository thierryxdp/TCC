def conta_frases(x):
    x = str.count(x,'...')
    x = str.count(x,'!')
    x = str.count(x,'?')
    x = str.count(x,'.')
    return (str.count(x,'...')+str.count(x,'!')+str.count(x,'?')+str.count(x,'.'))