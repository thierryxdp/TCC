def filtra_pares(a,b,c,d):
    '''Dada uma tupla com elementos do tipo int, a função
    retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original. tupla -> tupla'''
    s=(a,b,c,d)
    if s[0]%2==0:
        s=(a,)
    if s[1]%2==0:
        s=(a,b)
    if s[2]%2==0:
        s=(a,b,c)
    if s[3]%2==0:
        s=(a,b,c,d)
    return s