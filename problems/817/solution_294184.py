def acima_da_media(notas):
    """..."""
    if 5 in notas:
        notas.sort()
        x = list.index(notas, 5)
        return notas[x+1:]

    else:
        inclui5 = notas + [5]
        inclui5.sort()
        y = list.index(inclui5, 5)
        return inclui5[y+1:]