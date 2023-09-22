def conta_numero(numero,matriz):
    '''Retorna o numero de vezes que um numero esta presente em uma matriz
       parameters:
       numero: um numero inteiro qualquer
       matriz: matriz para analise
       int,list->int'''
    quantidade=[]
    for i in range(len(matriz)):
        for matriz[i] in matriz:
            quantidade+=[matriz[i].count(numero)]
        i+=1
        return sum(quantidade)
    if matriz==[]:
        return 0