def inverte(frase):
    '''Essa função recebe uma frase e retorna ela invertida e sem pontuação'''
    y= str.reverse(frase)
    a= str.replace(y,'.',' ')
    b= str.replace(a,'-',' ')
    c= str.replace(b,',',' ')
    d= str.replace(c,':',' ')
    e= str.replace(d,';',' ')
    f= str.replace(e,'?',' ')
    g= str.replace(f,'!',' ')
    return g