def media_matriz(matriz):
    s=0
    t=0
    for linha in matriz:
        s+=sum(linha)
        t+=len(linha)
    return round((s/t),2)