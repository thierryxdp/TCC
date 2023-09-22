def filtra_pares(inteiros):
"""retorna, dado uma tupla com 4 inteiros, uma nova tupla apenas com os elementos pares da tupla original, na ordem em que se encontravam
    tuple(int,int,int,int)--->tuple"""
    retorno=()
    if (inteiros[0])%2==0:
        retorno= retorno+(inteiros[0],)
    if (inteiros[1])%2==0:
        retorno= retorno+(inteiros[1],)
    if (inteiros[2])%2==0:
        retorno= retorno+(inteiros[2],)
    if (inteiros[3])%2==0:
        retorno= retorno+(inteiros[3],)
    return retorno