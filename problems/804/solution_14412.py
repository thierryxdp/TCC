def filtra_pares(a,b,c,d):
    """retorna apenas os números pares dentre os elementos da tupla de entrada"""
    """int, int, int, int -> tuple"""
    def par(x):
        if x%2==0:
        return x
    lista=(a,b,c,d)
    return filter(par,lista)