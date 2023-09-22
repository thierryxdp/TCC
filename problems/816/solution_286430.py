def maiores(numeros, n):
    """Função que, dada uma lista de números inteiros e um
    número inteiro n, retorna uma outra lista, que contém
    todos os números da lista original maiores que n, ordenados
    em ordem crescente.
    list, int -> list"""
    list.sort(numeros)
    posicao = list.index(numeros, n)
    return numeros[posicao:]