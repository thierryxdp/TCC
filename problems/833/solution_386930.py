def conta_numero(numero, matriz):
    a=[]
    for i in range (0,len(matriz)):
        for j in matriz[i]:
            if j==numero:
                a.append(j)
    return len(a)