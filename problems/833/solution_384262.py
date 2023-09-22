def conta_numero(numero,matriz):
    """funcao que define quantas vezes um 
    dado numero aparece na matriz fornecida
    entrada matriz_inteiro,saida_inteiro"""
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                c=c+1
            return c