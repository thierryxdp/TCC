def acima_da_media(lista):
    """fun ̧c~ao recebe lista e retorna lista ordenada
    list--> list"""
    media = int(sum(lista) / len(lista))
    return maiores(lista, media)