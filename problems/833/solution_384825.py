def conta_numero(matriz,n):
    contador = 0
    i = 0
    for i in matriz:
        for k in i:
            if k == n:
                contador += 1
    return contador