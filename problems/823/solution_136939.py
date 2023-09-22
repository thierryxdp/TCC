def faltante(lista):
    """
    Função que recebe um lista de números, se um número não estiver dentro daquele intervalo [1, N] retorna o número que está
    faltando.
    list -> int
    """
    contador = 0
    listaOrdenada = lista

    while contador < len(lista):
        if contador + 1 == listaOrdenada[contador]:
            contador += 1

        else:
            return contador + 1

    return contador + 1