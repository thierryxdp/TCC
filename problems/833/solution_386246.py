def conta_numero(numero,matriz):
    qtd_vezes=0
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(len(nlin)):
        for j in range(len(ncol)):
            if numero in matriz:
                qtd_vezes=qtd_vezes+matriz.count(numero)
    return qtd_vezes