def conta_numero(numero,matriz):
    for i in range(0,len(matriz)):
        quantidade = 0
        if numero in matriz[i]:
            quantidade +=1
    return quantidade