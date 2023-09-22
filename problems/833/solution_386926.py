def conta_numero(numero, matriz):
    a=[]
    for i in range (0,len(matriz)):
        for j in range (0,len(matriz[i])):
            if j==numero:
                a.append(numero)
    return len(a)