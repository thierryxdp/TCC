def acima_da_media(notas):
    """Retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list"""
    list.append(notas,6)
    list.sort(notas)
    posicao = list.index(notas,6)
    return notas[posicao+1:]