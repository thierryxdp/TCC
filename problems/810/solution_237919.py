def inverte(f):
    '''Função que tendo uma frase como entrada retorna essa frase na
    ordem inversa, sem letras maiúsculas e sem pontuação.
    str -> str'''
    m= str.lower(f)
    n= str.replace(m,'.',' ')
    n= str.replace(n,',',' ')
    n= str.replace(n,';',' ')
    n= str.replace(n,'!',' ')
    n= str.replace(n,'?',' ')
    n= str.replace(n,':',' ')
    n= str.replace(n,'-',' ')
    n= str.replace(n,'...',' ')
    s= str.split(n)
    v= s[::-1]
    j= str.join(' ',v)
    return j