def inversa(x):
    '''funçao que dada uma frase retorna a mesma na ordem inversa,
    sem letras maiusculas e sem a pontuação'''
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    f=str.lower(e)
    g=str.split(f)
    list.reverse(g)
    h=str.join(' ',g)
    return h