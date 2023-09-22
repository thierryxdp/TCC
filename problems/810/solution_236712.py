def inverte(string):
    '''Função que dada uma frase qualquer retorna ela ao contrário, com a
    letra inicial minúscula e sem pontuação. str -> str'''
    str.lower(string[0])
    a = str.replace(string,',',' ')
    b = str.replace(a,'.',' ')
    c = str.replace(b,'-',' ')
    d = str.replace(c,';',' ')
    e = str.replace(d,':',' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    x = str.split(g,' ')
    y = str(x)
    w = str.strip(y,'[')
    z = str.strip(w,']')
    t = str.join(z,z[::-1])
    return t