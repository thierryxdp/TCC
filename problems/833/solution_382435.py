def conta_numero(numero,matriz):
    quantidade=[]
    for i in range(len(matriz)):
        for numero in matriz:
            quantidade+=[matriz.count(numero)]
        i+=1
        return quantidade