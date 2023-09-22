def acima_da_media(lista):
    """essa"""
    media = sum(lista)/len(lista)
    maior = lista.count([:-1])> media
    return maior