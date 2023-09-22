def conta_numero(numero,matriz):
    num=0
    if len[matriz]=0:
        return 0
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if numero in matriz[i][j]:
                    num= num + 1
        return num