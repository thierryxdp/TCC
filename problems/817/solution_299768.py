def acima_da_media(notas):
    """Retorna uma lista ordenada com as notas que ficaram
    acima da média.
    list -> list"""
    m = sum(notas)//len(notas)
    if m not in notas:
        list.append(notas,m)
        list.sort(notas)
        posicao = list.index(notas,m)
        return notas[posicao+1:]
    else:
        list.sort(notas)
        posicao = list.index(notas,m)
        return notas[posicao+1:]