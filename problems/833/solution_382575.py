def conta_numero(numero,matriz):
    for i in matriz:
        for j in matriz:
            if numero in matriz[i][j]:
            return list.count(matriz[i][j],numero)