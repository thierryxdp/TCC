def lingua_p(pal):
    ''''''
    pal = pal.lower()
    i = 0
    tradu = []
    for n in pal:
        if n in 'aeiou':
            i += 1
            list.append(tradu, list(pal[:i+1]))
            list.append(tradu, 'p')
        else:
            i += 1
    return tradu