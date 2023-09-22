def maiores(lista,n):
    '''Esta e a funcao que dada uma lista de numeros
    inteiros e um numero inteiro n, retorna outra lista
    que contenha todos os numeros da lista original maiores
    que n ordenados.'''
    lista.append(n)
    lista.sort()
    lista.reverse()
    if n <int in lista:
        lista.remove(lista[n:])
        return lista