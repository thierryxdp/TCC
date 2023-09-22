def acima_da_media(lista):
    """..."""
    media = sum(lista)/len(lista)
    
    lista = [i for i in lista if n>= media]
    
    return lista