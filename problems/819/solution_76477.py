def filtraMultiplos(lista,n):
    """Funcao que calcula o numero de divisores"""
    lista = range(lista,0,-1)
    divisores = 0
    for count in lista:
        if n % count == 0:
            divisores = divisores + 1
    return divisores