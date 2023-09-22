def lingua_p(pal):
    i=0
    aux=''
    while i<len(pal):
        if pal[i] in 'aeiou':
            aux = aux + pal[i] + 'p' + pal[i]
        else:
            aux = aux + pal[i]
        i=i+1
    return aux