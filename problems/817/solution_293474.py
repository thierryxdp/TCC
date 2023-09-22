def acima_da_media(lista):
    '''Entre com uma lista de notas para retornar as notas que ficaram 
    acima da media
    Lista, Int -> Lista'''
    Nlista = lista
    media = (sum(Nlista))/2
    Nlista.insert(1, media)
    Nlista.sort()
    X = Nlista.index(media)

    return media