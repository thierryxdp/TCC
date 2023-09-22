def filtraMultiplos(lista,n):
    '''Recebe uma lista de números e um número inteiro n
    e retorna uma lista contendo todos os elementos da lista
    que são divisíveis por n.
    list, int -> list'''
    x = 0
    div = []
    while x < len(lista):
        if lista[x] % n == 0:
            div += lista[x]
        return div