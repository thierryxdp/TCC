def posLetra(frase,letra,n):
    a = 0
    fr = []
    while a <len(frase):
        if frase[a] == letra:
            fr += [frase.index(frase[a],a,len(frase))]
        a += 1
    if n >= len(fr):
        return fr[(n-1)]
    else:
        return -1