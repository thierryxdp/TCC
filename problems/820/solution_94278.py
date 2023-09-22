def posLetra(frase, letra, o):
    fraselist = []
    u = 0
    while u < len(frase):
        fraselist.append(frase[u])
        u=u+1
    i = 0
    indices = []
    while i < len(fraselist):
        if fraselist[i] == letra:
            indices.append(i)
        i=i+1
    if letra in frase:
        return indices[o-1]
    else:
        return -1