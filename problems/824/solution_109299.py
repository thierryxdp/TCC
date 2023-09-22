def poslehtra(frase,letra,oc):
    i = 0
    p = 0
    while(len(frase)>i):
        if frase[i] == letra:
            p = p + 1
        if p == oc:
            return i
        i = i + 1
    return -1