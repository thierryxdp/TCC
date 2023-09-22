def maiores(lista_numero,n):
    """dada uma lista de números inteiros e um número inteiro n, a função retorna uma outra lista que
    contenha todos os números da lista original maiores que n, ordenados em ordem crescente"""
    A=lista_numero
    list.append(A,n)
    list.sort(A)
    del A[:(n-1)]
    return A