def inverte(frase):
    '''Função que, a partir de uma frase, a retorna com as mesmas
    	palavras, porém com a ordem inversa, sem letras maiúsculas
        e sem pontuação'''
    x=frase.replace('...',' ')
    y=x.replace('.',' ')
    z=y.replace('!',' ')
    w=z.replace('?',' ')
    v=w.replace('-',' ')
    u=v.replace(';',' ')
    a=u.replace(':',' ')
    b=a.replace(',',' ')
    c=str.lower(b)
    d=str.split(c)
    list.reverse(d)
    e=str.join('-',d)
    f=e.replace('-',' ')
    return f