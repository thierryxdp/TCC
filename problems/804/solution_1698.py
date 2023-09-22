def filtra_pares(x):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple(int,int,int,int)"""
    tup = ()
    if x[0]%2 == 0:
        tup = tup + (x[0])
    if x[1]%2 == 0:
        tup = tup + (x[1])
    if x[2]%2 == 0:
        tup = tup + (x[2])
    if x[3]%2 == 0:
        tup = tup + (x[3])