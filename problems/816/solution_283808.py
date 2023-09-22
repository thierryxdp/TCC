def maiores(lista,n):
    """Dada a lista de números inteiros e o número inteiro n,
    a função retorna uma lista que contenha todos os elementos
    da lista original maiores que n, ordenados em ordem crescente.
    Parametros de Entrada: list
    Retorna: list"""

    list.append(lista,n)
    list.sort(lista)

    auxiliar= list.index(lista,n)
    listaSaida= lista[auxiliar+1:]

    return listaSaida