def inverte(f):
    '''
    Função que dada uma frase retorna uma outra frase contendo as mesmas palavras na
    ordem inversa, sem letras maiúsculas, e sem pontuação.
    str-> lista
    '''
    y=str.replace(f,'-',' ')
    z=str.replace(y,',',' ') 
    w=str.replace(z,':',' ')
    n=str.replace(w,';',' ')
    k=str.replace(n,'.',' ')
    c=str.replace(k,'?',' ')
    v=str.replace(c,'!',' ')
    x=(v[::-1])
    contrario=(str.lower(x))
    return contrario