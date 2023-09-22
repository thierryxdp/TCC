def maiores(lista, n):
    '''Entre com uma lista de numeros e um numero inteiro para retornar os
    valores maiores que o inteiro
    Lista, Int -> Lista'''
    Nlista = lista
    Nlista.insert(1, n)
    Nlista.sort()
    X = Nlista.index(n)

    return Nlista[X:]