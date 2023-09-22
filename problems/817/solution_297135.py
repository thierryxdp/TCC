def acima_da_media(lista,k):
    """list-> list"""
    media= k* sum(lista)/len(lista)
    return maiores(lista, media)