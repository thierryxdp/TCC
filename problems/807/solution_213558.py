def conta_frases(texto):
    '''dado um texto, retorna o número de frases;
    str --> int'''
    s=str.join('/',str.split(texto,'...'))
    p=str.join('/',str.split(s,'?'))
    d=str.join('/',str.split(p,'!'))
    e=str.join('/',str.split(d,'.'))
    f=str.split(str.rstrip(e,'/'),'/')
    return len(f)