def lingua_p(pal):
    2i=0
    aux=''
    while i<len(pal):
        if str.lower(pal[i]) in 'aeiouáéíóúàèìòùãõ':
            aux = aux + pal[i] + 'p' + pal[i]
        else:
            aux = aux + pal[i]
            i=i+1
    return str.lower(aux)