def lingua_p(pal):
    ''''''
    pal = pal.lower()
    i = 0
    ulvog = 0
    tradu = []
    for n in pal:
        if n in 'aeiou':
            i += 1
            list.append(tradu, list(pal[ulvog:i]))
            list.append(tradu, 'p')
            ulvog = n
        else:
            i += 1
    return tradu