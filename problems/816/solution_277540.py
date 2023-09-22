def maiores(lista,n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contenha todos os números da lista original maiores que n
       list, int-> list"""
    outralista=lista[:]
    outralista=[elem for elem in lista if elem >= n]
    outralista.sort()
    return outralista