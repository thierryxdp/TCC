def Filtra_pares(x):
    """dado uma tupla com 4 elementos inteiros como entrada retorna apenas os parametros.
    entradas:tupla[0:4]
    saida:tupla[int(pares)]"""
    
    n = ()
    n0,n1,n2,n3=x
    
    if n0%2==0:
        n=n +(n0,)
    if n1%2==0:
        n=n +(n1,)
    if n2%2==0:
        n=n +(n2,)
    if n3%2==0:
        n=n +(n3,)
    return n