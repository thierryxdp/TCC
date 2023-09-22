def filtraMultiplos(lista,n):
    ''' funcao que dada uma lista de numeros inteiros e numero n, retorna os numeros da lista multiplos de n'''
    '''lista -> lista'''
    lista2 = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            lista2 = lista2 + [lista[proximo]]
        proximo = proximo + 1
    return lista2