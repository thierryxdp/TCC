def posLetra(oracao, letra, a):
    lista1 = []
    u = 0
    while u < len(oracao):
        lista1.append(oracao[u])
        u=u+1
    i = 0
    indices = []
    while i < len(lista1):
        if lista1[i] == letra:
            indices.append(i)
        i=i+1
    if a > len(indices):
        return -1
    else:
        return indices[a-1]