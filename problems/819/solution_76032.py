def filtraMultiplos(lista, n):
    '''Função que dada uma lista de números e um número n, retorna outra
    lista contendo os números que sejam múltiplos de n. list, int -> list'''
    lista1 = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            lista1 = lista1 + [lista[proximo],]
        proximo = proximo + 1
    return lista1