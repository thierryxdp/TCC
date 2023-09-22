def maiores(lista,n):
    """função que recebe uma lista de números inteiros e um número inteiro n e retorna
    todos os números da lista original maiores que n. list, int -> list"""
    list.append(lista,n)
    list.sort(lista)
    i = list.index(lista,n)
    novalista = lista[i+1:]
    return novalista