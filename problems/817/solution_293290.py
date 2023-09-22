def acima_da_media(notas):
    media = sum(notas)//len(notas)
    notasx = sorted(notas)
    y = notasx.index(media)
    if media in notasx:
        notas.append(media)
        return notasx[y+1:]
    else:
        return notasx[y+1:]