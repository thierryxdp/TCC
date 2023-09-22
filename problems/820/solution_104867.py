def posLetra(frase, l, o):
    lista = range(len(frase))
    r = []
    for e in lista:
        r.append([e, frase[e]])

    ocorrencias = []
    for i in range(len(r)):
        if r[i][1]== l:
            ocorrencias.append(r[i])

    if len(ocorrencias)>= o:
        return ocorrencias[o-1][0]
    return -1