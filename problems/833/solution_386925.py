def conta_numero(numero, matriz):
    a=[]
    for i in (0,len(matriz)):
        for j in (0,len(matriz[i])):
            if j==numero:
                a.append(numero)
    return len(a)