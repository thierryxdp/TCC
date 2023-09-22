def filtraMultiplos(lista,n):
    '''Recebe uma lista de números e um número inteiro n
    e retorna uma lista contendo todos os elementos da lista
    que são divisíveis por n.
    list, int -> list'''
    x = 0
    numeros = []
    while x < len(lista):
        x += 1
        if lista[x] % n == 0:
            numeros += [lista[x]]
        return numeros