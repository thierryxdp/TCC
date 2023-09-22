def acima_da_media(lista):
    """essa"""
    media = sum(lista)/len(lista)
    maior = [lista > media for lista in lista]
    return maior