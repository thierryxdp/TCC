def insere(lista_numero: list, n: int) -> list:
    """Dada uma lista ordenada de números inteiros e um número inteiro, inclui
       o número inteiro na posição correta da lista ordenada

       Parameters:
       lista_numero: Lista de números inteiros, ordenada na forma crescente
       n: Número inteiro a ser inserido na lista

       Return:
       Dados os parâmetros "lista_numero" e "n", adiciona o parâmetro "n" no
       parâmetro "lista_numero", de forma que esta continue ordenada na forma
       crescente

       Examples:
       insere([1, 2, 3], 4) == [1, 2, 3, 4]
       insere([10, 20, 30], 15) == [10, 15, 20, 30]
       insere([1, 4, 10, 100], 7) == [1, 4, 7, 10, 100]
    """

    list.append(lista_numero, n)
    list.sort(lista_numero)

    return lista_numero