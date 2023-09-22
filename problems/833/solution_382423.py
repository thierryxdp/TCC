def conta_numero(numero,matriz):
    quantidade=[]
    for posicao in range(len(matriz)):
        for numero in matriz[posicao]:
            quantidade+=[matriz[posicao].count(numero)]
        posicao+=1
        return sum.quantidade