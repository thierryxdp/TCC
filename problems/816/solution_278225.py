def maiores(lista, n):
    """Função que dada uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista que contenha todos os numeros da lista original maiores
    que n.
    Dados de entrada: list, int.
    Dados de saida: list."""
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista, n) + 1:]