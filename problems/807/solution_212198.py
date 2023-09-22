def quantas_frases(x):
    return str.count(x,'.')-str.count(x,'..')+str.count(x,'!')+str.count(x,'?')+str.count(x,'...')