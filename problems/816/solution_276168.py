def maiores(lista,n):
    """Esta é a função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n, list, int -> list"""
    x= sorted(lista)
    return [i for i in x if i > n]