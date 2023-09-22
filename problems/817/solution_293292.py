def acima_da_media(notas):
    media = sum(notas)//len(notas)
    notasx = sorted(notas)
    y = notasx.index(media)
    if media in notasx:
        notas.append(media)
        h = notasx.index(media)
        return notasx[h+1:]
    else:
        return notasx[y+1:]