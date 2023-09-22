def acima_da_media(lista,k):
    """list-> list"""
    media= sum(lista)/len(lista)
    return maiores(lista, media)