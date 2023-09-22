def filtra_pares(n1,n2,n3,n4):
    """retorna apenas elementos pares dos números
impostos, na mesma ordem em que se encontravam
int,int,int,int -> int,int,int,int"""  #posto 4 'int' de forma geral
    if n1%2 == 0:
        n1 = n1
    else:
        n1 =''
        
    if n2%2 == 0:
        n2 = n2
    else:
        n2 = ''
        
    if n3%2 == 0:
        n3 = n3
    else:
        n3 = ''
        
    if n4%2 == 0:
        n4 = n4
    else:
        n4 = ''
    
    return (n1,n2,n3,n4)