def maiores(numeros,n):
    """dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista original maiores que n, ordenados em ordem crescente."""
    list.append(numeros,n)
    list.sort(numeros)
    inicio = list.index(numeros,n)
    return numeros[inicio + 1:]