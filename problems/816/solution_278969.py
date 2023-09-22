def maiores(lista: list, n: int) -> list:
    """Dada uma lista de números inteiros e um número inteiro, retorna outra
       lista contendo todos os números da lista de números inteiros maiores que
       o número inteiro dado

       Parameters:
       lista: Lista de números inteiros
       n: Número inteiro qualquer a ser usado como referência

       Return:
       Dados os parâmetros "lista" e "n", retorna uma nova lista que contenha
       todos os números da lista do parâmetro "lista" maiores que o parâmetro
       "n"

       Examples:
       maiores([1, 6, 3, 8, 2], 4) == [6, 8]
       maiores([1, 2, 3, 4, 5, 7, 8], 6) == [7, 8]
       maiores([10, 2, 54, 5, 20], 8) == [10, 20, 54]
    """

    list.append(lista, n)
    list.sort(lista)
    x = list.index(lista, n)
    y = lista[x + 1:]

    return y