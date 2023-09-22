def lingua_p(pal):
    i=0
    aux=''
    while i<len(pal):
        if pal[i] == 'a':
            aux = aux + pal[i] + 'p' + pal[i]
        elif pal[i] == 'e':
            aux = aux + pal[i] + 'p' + pal[i]
        elif pal[i] == 'i':
            aux = aux + pal[i] + 'p' + pal[i]
        elif pal[i] == 'o':
            aux = aux + pal[i] + 'p' + pal[i]
        elif pal[i] == 'u':
            aux = aux + pal[i] + 'p' + pal[i]
        else:
            aux = aux + pal[i]
        i=i+1
    return aux