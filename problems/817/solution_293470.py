def acima_da_media(lista):
    '''Entre com uma lista de numeros e um numero inteiro para retornar os
    valores maiores que o inteiro
    Lista, Int -> Lista'''
    Nlista = lista
    Nlista.insert(1, 5)
    Nlista.sort()
    X = Nlista.index(5)+1

    return Nlista[X:]