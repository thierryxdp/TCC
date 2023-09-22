def inverte(frase):
    """Retorna a frase de entrada invertida; str->str"""
    a = str.replace(frase, '.', ' ')
    b = str.replace(a, '!', ' ')
    c = str.replace(b, '?',' ')
    d = str.replace(c, '...',' ')
    e = str.replace(d, '-', ' ')
    f = str.replace(e, ',', ' ')
    g = str.replace(f, ':', ' ')
    h  = str.replace(g, ';', ' ')
    i = str.lower(h)
    j = str.split(i)
    k = list.reverse(j)
    l = str.join(' ', j)
    frase = l
    return frase