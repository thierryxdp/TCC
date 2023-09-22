def conta_frases(texto):
    if str.find(texto,'...')==-1:
        return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')
    elif str.find(texto,'...')==1:
        return str.count(texto,'...')+str.count(texto,'!')+str.count(texto,'?')-2*str.count(texto,'.')
    elif str.find(texto,'...')>1:
        return str.count(texto,'...')+str.count(texto,'!'+str.count(texto,'.')