def conta_numero(numero, matriz):
    '''dado um numero inteiro e uma matriz de numeros inteiros, conta e retorna quantas vezes aquele numero aparece na matriz'''
    qtd_vezes = []
    nlin=len(matriz)
    ncol=len(matriz)
    for i in range(nlin):
        for j in range(ncol):
            if numero in matriz:
                qtd_vezes=qtd_vezes+matriz.count(numero)
                return qtd_vezes