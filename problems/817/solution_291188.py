def acima_da_media(lista):
    """..."""
    media = sum(lista)/len(lista)
    
    lista = [i for i in lista if i>= media]
    
    return lista