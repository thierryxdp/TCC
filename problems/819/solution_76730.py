def filtraMultiplos(lista, n):
    """Função que dada uma lista qualquer, retorna outra lista contendo apenas os números que são divisíveis por um inteiro qualquer n
    (list, int) -> list """
    lista_multiplos_n = []
    i = 0

    while i <= len(lista) - 1:
        if lista[i] % n == 0:
            list.append(lista_multiplos_n, lista[i])
        i = i + 1

    return lista_multiplos_n