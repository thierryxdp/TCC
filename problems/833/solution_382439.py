def conta_numero(numero,matriz):
    quantidade=[]
    for i in range(len(matriz)):
        for matriz[i] in matriz:
            quantidade+=[matriz[i].count(numero)]
        i+=1
        return sum(quantidade)
    if matriz==[]:
        return 0