def filtraMultiplos(lista: list, n: int) -> list:
    """Filtra os múltiplos de um número, dada uma lista e um número

       Parameters:
       lista: Lista formada por números
       n: Número inteiro qualquer

       Return:
       Dados os parâmetros "lista" e "n", retorna todos os números do parâmetro
       "lista" que são divisíveis pelo parâmetro "n"

       Examples:
       filtraMultiplos([4], 2) == [4]
       filtraMultiplos([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
       filtraMultiplos([1, 3, 5, 7], 2) == []
    """

    multiplos = []
    i = 0

    while i < len(lista):
        if ((lista[i] % n) == 0):
            list.append(multiplos, lista[i])
        i = i + 1

    return multiplos