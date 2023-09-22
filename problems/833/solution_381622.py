def conta_numero(numero, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero in matriz:
                M = matriz[i][j]
                ocorrencia = list.append(list.count(M, numero))
                return ocorrencia
            else:
                return 0