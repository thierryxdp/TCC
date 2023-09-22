def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    lista= [frase]
    y= list.reverse(lista) 
    a= list.remove(y, '.')
    b= list.remove(a, '-')
    c= list.remove(b, ',')
    d= list.remove(c, ':')
    e= list.remove(d, ';')
    f= list.remove(e, '?')
    g= list.remove(f, '!')
    return g