def conta_numero(numero,matriz):
    recorrenciatotal=0
    for i in len(matriz):
        recorrencia=0
        for j in range(len(matriz[0])):
            if matriz[j]==numero:
        		recorrencia+=1
    recorrenciatotal+=recorrencia
    return recorrenciatotal