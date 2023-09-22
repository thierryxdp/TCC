def conta_numero(matriz,numero):
    """A funcao conta_numero recebe como entrada uma matriz e um numero, e retornará
    o numero de ocorrências deste numero na matriz.
    ent: list, int -> ret: int."""
    pos = 0
    conta = 0
    for pos in range(len(matriz)):
        conta += list.count(matriz[pos],numero)
    return conta