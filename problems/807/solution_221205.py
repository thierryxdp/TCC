def conta_frases(texto):
    '''funcão que calcula a quantidade de frases separadas por um ponto final'''
    b=str.replace(texto,'!','.')
    c=str.replace(b,'?','.')
    d=str.replace(c,'...','.')
    a=str.split(d,'.')
    return len(a)-1