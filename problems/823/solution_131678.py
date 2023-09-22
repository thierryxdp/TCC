def faltante(lista):
    """
    Funçao que recebe uma lista de números, se um número não estiver dentro daquele intervalo [1, N] retorna o número que está
    faltando.
    list -> int
    """
    c= 0
    listaOrd= sorted(lista)

    while c < len(lista):
        if c + 1 == listaOrd[c]:
            c += 1

        else:
            return c 

    return c