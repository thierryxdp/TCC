def par(n):
    """ dada  um numero -------- retornaremos true caso for par e caso contrario
        retornaremos false
        entrada -->int?,float?
        saida   --> bool """
    if n%2==0:
        return True
    else:
        return False
def filtra_pares(a):
    """ Dado uma tupla com 4 elementos retornaremos uma nova tupla com os
        numeros pares.
        entrada --> int
        saida   --> int """
    return tuple(filter(par,a))