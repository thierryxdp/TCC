def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    lista= [frase]
    lista2= list.reverse(lista) 
    a= list.remove(lista2, '.')
    b= list.remove(a, '-')
    c= list.remove(b, ',')
    d= list.remove(c, ':')
    e= list.remove(d, ';')
    f= list.remove(e, '?')
    g= list.remove(f, '!')
    return g