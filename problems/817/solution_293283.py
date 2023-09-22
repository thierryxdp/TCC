def acima_da_media(notas):
    media = sum(notas)//len(notas)
    notasx = sorted(notas)
    notasx.append(media)
    y = notasx.index(media)
    return notasx[y+1:]