def filtra_pares(tupla):
    """
    Recebe uma tupla com quatro elementos inteiros e retorna uma nova
    tupla contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam.
    tupla(int, int, int, int) -> tupla(int, int, int, int) ou tupla(int, int, int)
    ou tupla(int, int) ou tupla(int,)
    """
    pares=()
    if tupla[0]%2==0:
        pares=tupla[0],
    if tupla[1]%2==0:
        pares2=tupla[1],
        pares=pares+pares2
    if tupla[2]%2==0:
        pares3=tupla[2],
        pares=pares+pares3
    if tupla[3]%2==0:
        pares4=tupla[3],
        pares=pares+pares4
    return pares