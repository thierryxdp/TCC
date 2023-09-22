def faltante (pecas) :
    """Funcao que dada uma lista com N - 1 inteiros enumerados de 1 a N, retorna qual numero inteiro deste intervalo esta faltando"""
    list.sort(pecas)
    if pecas[0] != 1:
        return 1

    listaN = list(range(pecas[0],pecas[-1]+1))
    if listaN == pecas:
        return pecas[-1] + 1

    contador = 0
    while contador < len(listaN):
        if listaN[contador] != pecas[contador]:
            return listaN[contador]

        contador = contador + 1

    else:
        return contador - 1