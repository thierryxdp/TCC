def acima_da_media(lista):
    """list-> list"""
    media= sum(lista)/len(lista)
    return maiores(lista, media)