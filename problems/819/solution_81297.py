def filtraMultiplos(lista, numero):

    """Filtra uma lista de números inteiros, retornando apenas os que são múltiplos de um dado número.

    Entrada: lista, int

    Saída: lista

    """

    indice = 0

    filtro = []

    while indice < len(lista):

        if lista[indice]%numero == 0:

            list.append (filtro, lista[indice])

        indice = indice + 1

    return filtro