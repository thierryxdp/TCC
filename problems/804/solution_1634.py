#Start your python function here
def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam
    tupla(int,int,int,int) -> tupla
    '''
    n1,n2,n3,n4 = tupla
    
    if n1%2==0:
        a = (n1,)
    else:
        a = ()
    if n2%2==0:
        b = (n2,)
    else:
        b = ()
    if n3%2==0:
        c = (n3,)
    else:
        c = ()
    if n4%2==0:
        d = (n4,)
    else:
        d = ()
        
    return a+b+c+d