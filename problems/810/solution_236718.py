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
    p = x[-1::-1]
    y = str(p)
    j = str.strip(y,'[')
    l = str.strip(j, ',')
    m = str.strip(l,']')
    n = str.strip(m,',')
    o = str.strip(n,',')
    k = str.strip(o,"'")
    return k