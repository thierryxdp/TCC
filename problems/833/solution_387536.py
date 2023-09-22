def conta_numero(numero,matriz):
    quantidade = 0
    for i in range(0,len(matriz)):
        if numero in matriz[i]:
            quantidade +=1
    return quantidade