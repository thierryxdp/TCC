def lingua_p(pal):
    i=0
    aux=''
    while i<len(pal):
        if pal[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            aux = aux + pal[i] + 'p' + pal[i]
        else:
            aux = aux + pal[i]
        i=i+1
    return aux