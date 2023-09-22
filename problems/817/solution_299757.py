def acima_da_media(notas):
    """Retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list"""
    media = sum(notas)/len(notas)
    list.sort(notas)
    posicao = list.index(notas,media)
    return notas[posicao:]