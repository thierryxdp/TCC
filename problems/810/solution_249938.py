def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    lista= [frase]
    lista2= list.reverse(lista)
    y= " ".join(lista2) 
    a= str.replace(y,'.',' ')
    b= str.replace(a,'-',' ')
    c= str.replace(b,',',' ')
    d= str.replace(c,':',' ')
    e= str.replace(d,';',' ')
    f= str.replace(e,'?',' ')
    g= str.replace(f,'!',' ')
    return g