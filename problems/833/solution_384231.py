def conta_numero(numero,matriz):
    """funcao que define quantas vezes um 
    dado numero aparece na matriz fornecida
    entrada matriz inteiro saida inteiro"""
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if numero in matriz[i][j]:
                c=c+1
                return c