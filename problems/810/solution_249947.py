def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    y= str.lower(frase)
    a= str.replace(y,'.',' ')
    b= str.replace(a,'-',' ')
    c= str.replace(b,',',' ')
    d= str.replace(c,':',' ')
    e= str.replace(d,';',' ')
    f= str.replace(e,'?',' ')
    g= str.replace(f,'!',' ')
    lista= g.split()
    list.reverse(lista)
    lista2= str.join(' ',lista)
    return lista2