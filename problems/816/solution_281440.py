def maiores(lista_numeros,n):
    """funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna uma lista que contenha todos os numeros da lista original maiores que n
    list(int),int--->list(int)"""
    lista_numeros=lista_numeros+[n]
    list.sort(lista_numeros)
    return lista_numeros[n+1:]