def inverte(string):
    '''Função que dada uma frase qualquer retorna ela ao contrário, com a
    letra inicial minúscula e sem pontuação. str -> str'''
    v = str.lower(string)
    a = str.replace(v,',','')
    b = str.replace(a,'.','')
    c = str.replace(b,'-','')
    d = str.replace(c,';','')
    e = str.replace(d,':','')
    f = str.replace(e,'!','')
    g = str.replace(f,'?','')
    x = str.split(g,' ')
    p = x[0::-1]
    k = ' '.join(p)
    return k