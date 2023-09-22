def maiores(numeros, n):
    """Função que, dada uma lista de números inteiros e um
    número inteiro n, retorna uma outra lista, que contém
    todos os números da lista original maiores que n, ordenados
    em ordem crescente.
    list, int -> list"""
    list.append(numeros, n)
    list.sort(numeros)
    posicao = list.index(numeros, n)
    lista = numeros[posicao:]
    list.remove(lista, n)
    return lista