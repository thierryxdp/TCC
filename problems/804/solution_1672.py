def filtra_pares(x,y,z,w):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple"""
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return x,y,z,w
    else:
        return ()