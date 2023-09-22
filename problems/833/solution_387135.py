def conta_numero(numero:int,matriz:list)->int:
    """dado um número inteiro e uma matriz, conta quantas vezes o número aparece na mesma"""
    contanum=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                contanum+=1
    return contanum