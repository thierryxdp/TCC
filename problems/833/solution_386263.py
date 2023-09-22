def conta_numero(numero,matriz):
    qtd_vezes=0
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            for numero in matriz:
                if (numero==nlin)and(numero==ncol):
                    qtd_vezes+=matriz.count(i)
                i=i+1   
    return qtd_vezes