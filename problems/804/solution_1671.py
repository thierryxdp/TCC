def filtra_pares(x,y,z,w):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple"""
    if x%2==0:
        return x
    elif y%2==0:
        return y
    elif z%2==0:
        return z
    elif w%2==0:
        return w