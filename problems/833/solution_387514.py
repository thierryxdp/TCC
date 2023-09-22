def conta_numero(numero,matriz):
    quantidade = 0
    for i in matriz:
        for j in matriz[i]:
            quantidade +=1
    return quantidade