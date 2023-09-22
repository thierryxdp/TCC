def conta_frases(x):
    frases= str.count(x,'!')+str.count(x,'?')
    resultado=frases+(str.count(x,'.')-str.count(x,'...')-str.count(x,'...'))
    return resultado