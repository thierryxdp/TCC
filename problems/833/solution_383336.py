def conta_numero(numero,matriz):
    '''Função que recebe uma matriz e um numero e retorna quantas vezes o numero apareceu na matriz
    Entrada(matriz,int)
    Saída(int)'''
    cont=0
    for i in matriz:
        for j in i:
            if j==numero:
                cont+=1
    return cont