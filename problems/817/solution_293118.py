def acima_da_media(nota):
    """retorna uma lista ordenada com as notas que ficaram acima da media
    list -> list"""
    
    media = sum(nota)//len(nota)
    dentro_media = (nota) < (media)
    dentro_media = list.sort(dentro_media)

    return dentro_media