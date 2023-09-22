def maiores(lista, n):
    '''Calcula e retorna, a partir de uma lista original, uma lista composta pelos numeros da primeira lista maiores que o numero inteiro acrescentado a ela
    parameters:
    lista:lista original
    n:numero inteiro acrescentado
    list, int -> list'''
    lista.append(n)
    lista.sort()
    posicao=lista.index(n)
    return lista[posicao+1:]