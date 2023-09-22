def conta_numero(numero,matriz):
    quantidade=[]
    for i in range(len(matriz)):
        for numero in matriz[i]:
            quantidade+=[matriz[i].count(numero)]
            i+=1
        return quantidade