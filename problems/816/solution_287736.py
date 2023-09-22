def maiores(lista,n):
    """dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n ordenados em ordem crescente"""
    list.extend(lista,n)
    list.sort(lista)
    return lista[n+1:]