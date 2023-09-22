def filtra_pares(x):
    '''função que recebe uma tupla x com 4 números inteiros como argumentos,
e retorna uma tupla contendo apenas os elementos pares, na ordem da tupla
original; Entrada: tuple(int,int,int,int); Retorno:tuple(vazio ou com int)'''
    (a,b,c,d)=x
    def par(y):
        if y/2 == y//2:
            return True
        else:
            return False
    return tuple(filter(par,x))