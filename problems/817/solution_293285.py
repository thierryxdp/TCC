def acima_da_media(notas):
    media = sum(notas)//len(notas)
    notas.append(media)
    notasx = sorted(notas)
    y = notasx.index(media)
    return notasx[y+1:]