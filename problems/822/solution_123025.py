def repetidos(lista):
    """Função que retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list -> int """
    i = 1
    n = 0

    while i - 1 <= len(lista) - 2:
        if lista[i-1] == lista[i]:
            n = n + 1

        i = i + 1

    return n