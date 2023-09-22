#Filtragem
def filtra_pares(a,b,c,d):
    '''Esta função retorna uma nova tupla apenas com os valores
    pares de uma tupla dada.
    int, int, int, int -> int'''
    if (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        return (a,b,c,d)