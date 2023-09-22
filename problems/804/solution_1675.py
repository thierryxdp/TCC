def filtra_pares(x):
    """Função que, ao receber uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
    tuple(int,int,int,int)->tuple"""
    if x[0]%2==0:
        return x[0]
    elif x[1]%2==0:
        return x[1]
    elif x[2]%2=0:
        return x[2]
    elif x[3]%2==0:
        return x[3]
    else:
        return ()