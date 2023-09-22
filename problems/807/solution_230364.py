def conta_frases(frase):
    ls=str.count(frase,'...')+str.count(frase,'?')+str.count(frase,'!')
    if('.' not in frase):
        return ls
    return str.count(frase,'.')+ls