def filtra_pares(numeros):
    """retorna apenas elementos pares dos números
impostos, na mesma ordem em que se encontravam
int,int,int,int -> int,int,int,int"""  #posto 4 'int' de forma geral
    n = () #criando uma tupla vazia
    n1,n2,n3,n4 = numeros
    if n1 %2 == 0:
        n = n + (n1,)
    if n2 % 2 == 0:
        n = n +(n2,)
    if n3 % 2 == 0:
        n = n + (n3,)
    if n4 % 2 == 0:
        n= n + (n4,)
    return n