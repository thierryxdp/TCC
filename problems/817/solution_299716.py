def acima_da_media(notas: list) -> list:
    '''
    Retorna lista ordenada com as notas que ficaram acima da média dada uma lista com as notas
    '''
    media = sum(notas) / len(notas)
    notas.append(media)
    notas.sort()
    a = notas.index(media)
    return notas[a:]