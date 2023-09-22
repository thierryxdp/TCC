def acima_da_media(lista):
    '''Entre com uma lista de notas para retornar as notas que ficaram 
    acima da media
    Lista, Int -> Lista'''
    Nlista = lista
    Nlista.insert(1, 5)
    Nlista.sort()
    X = Nlista.index(5)+1

    return Nlista[X:]