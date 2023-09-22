def inverte(frase):
    '''função que retorna um tal frase ,porem invertida'''
    '''str->str'''
    a = str.replace(frase,'-',' ')
    b = str.replace(a, ',', ' ')
    c = str.replace(b, ':', ' ')
    d = str.replace(c, ';', ' ')
    e = str.replace(d, '.', ' ')
    f = str.replace(e, '?', ' ')
    g = str.replace(f, '!', ' ')
    h = g.lower()
    i = str.split(h)[-1::-1]
    j = i.join(' ',i)
    return j