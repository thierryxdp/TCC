def maiores(numeros,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista que contém todos os números da lista original maiores que n, ordenados em ordem crescente: list,int -> list'''
    if n in numeros:
        numeros.sort()
        lista1 = numeros[list.index(numeros,n):]
        return lista1
    if n not in numeros:
        numeros.sort()
        if n < numeros[0]:
            return numeros
        if n >= numeros[-1]:
            return []