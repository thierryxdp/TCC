def media_matriz(x):
    som=0
    tam=0
    for l in x:
        som+=sum(l)
        tam+=len(l)
    return round(som/tam,2)