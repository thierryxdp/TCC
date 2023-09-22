def filtra_pares (a,b,c,d):
    """essa função recebe uma tupla com 4 elementos de entrada e devolve apenas os números pares;
    int,int,int,int--->int"""
    lista1 = [a,b,c,d]
    lista2 = sorted(filter(lambda x: x% 2 == 0, lista1))
    return lista2