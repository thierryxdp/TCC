def maiores(lista,n):
    '''Esta e a funcao que dada uma lista de numeros inteiros
    e um numero inteiro n, retorna outra lista que contenha
    todos os numeros da lista original maiores do que n
    ordenados em ordem crescente'''
    numeros = list()
    for num in lista:
        if num >= n:
            numeros.append(num)
            numeros.sort()
    return numeros