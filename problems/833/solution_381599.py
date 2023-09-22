def conta_numero(numero, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                       m = matriz[i][j]
                       c = list.count(m, numero)
   				return c