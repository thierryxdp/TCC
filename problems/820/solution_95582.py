def posLetra(frase,letra,n):
    a = 0
    fr = []
    while a <len(frase):
        if frase[a] == letra:
            fr += [str.index(frase[a])]
        a += 1
    return fr[(n-1)]