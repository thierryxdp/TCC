#Start your python function here
def filtra_pares(tupla):
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam
    tupla(int,int,int,int) -> tupla
    '''
    n1,n2,n3,n4 = tupla
    
    if n1%2==0:
        a = n1
    elif n1%2!=0:
        a = ()
    elif n2%2==0:
        b = n2
    elif n2%2!=0:
        b = ()
    elif n3%2==0:
        c = n3
    elif n3%2!=0:
        c = ()
    elif n4%2==0:
        d = n4
    elif n4%2!=0:
        d = ()
        
    return a+b+c+d