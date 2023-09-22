def conta_numero(numero,matriz):
    """Recebe um numero inteiro e uma matriz e retorna quantas vezes o número aparece na matriz/int,list->int"""
    cont1=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                cont1+=1
    return cont1