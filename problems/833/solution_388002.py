def conta_numero(num,matriz):
    '''dado um numero inteiro e uma matriz de numeros inteiros, conta e retorna quantas vezes aquele numero aparece na matriz'''
    qtd_vezes=0
    nlin=len(matriz):
        ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if num in matriz:
                qtd_vezes=qtd_vezes+matriz.count(num)
    return qtd_vezes