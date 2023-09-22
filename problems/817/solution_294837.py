def acima_da_media(lista):
    import math
    lista.sort()
    media= math.ceil(len(lista)/2 )
    resultado = lista[media:]
    return  (resultado)