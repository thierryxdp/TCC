def inverte(frase):
    ''' Funcao que dada uma frase retorna uma segunda frase
    que possui todas as palavras da frase primaria na ordem
    inversa.
    Parametros:
    Str
    Saida: Str
    '''
    h= str.replace(frase,'.',' ')
    i= str.replace(h,'!',' ')
    j= str.replace(i,'...',' ')
    k= str.replace(j,'?',' ')
    l= str.replace(k,',','')
    m= str.replace(l,'-',' ')
    n= str.replace(m,':',' ')
    o= str.replace(n,';',' ')
    p= str.lower(o)
    q= str.split(p)
    r= q[::-1]
    s= str.join(' ',r)
    

    return s