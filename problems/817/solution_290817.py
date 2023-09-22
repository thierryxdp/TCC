def acima_da_media(lista):
    """essa"""
    n_elementos = len(lista)
    media = sum(lista)/n_elementos
    lista_maiores = ()
    return len([n for n in lista if n < media])