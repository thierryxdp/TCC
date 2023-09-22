def conta_numero(numero,matriz):
    '''função que conta e retorna quantas vezes o número
    informado aparece na matriz. int, list-> int'''
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                cont=cont+1
    return cont