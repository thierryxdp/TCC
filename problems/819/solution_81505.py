def filtramultiplos(lista,n):
    '''função de uma lista ñ vazia,
    lista --> lista'''
    lista2 = []
    proximo = 0
    while proximo <len (lista):
        if lista[proximo]%n == 0:
            lista2 = lista2 + [lista[proximo]]
        proximo= proximo + 1
    return lista2