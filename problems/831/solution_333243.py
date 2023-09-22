def lingua_p(pal):
    i=0
    aux=''
    while i<len(pal):
        if pal[i] != 'a' or 'e':
            aux = aux + pal[i]
        else:
            aux = aux + pal[i] + 'p' + pal[i]
        i=i+1
    return aux