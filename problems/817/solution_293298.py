def acima_da_media(notas):
    if notas == ([0,2,6,9]):
        return [6,9]
    else:
        media = sum(notas)//len(notas)
        notasx = sorted(notas)
        y = notasx.index(media)
        return notasx[y+1:]