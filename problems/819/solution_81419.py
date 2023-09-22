def filtraMultiplos(lista,n):
    '''Essa função filtrar os múltiplos de um número n, dado o valor de entrada uma lista de números e um número'''
    ''' list,int -> list'''
    lista2 = []
    proximo = 0
    while proximo < len(lista):
        if lista [proximo]%n == 0:
            lista2 = lista2 + [lista[proximo]]
        proximo = proximo + 1
    return lista2