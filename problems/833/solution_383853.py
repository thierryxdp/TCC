def conta_numero(numero:int,matriz:list)->int:
    """ A função recebe como entrada um número e uma matriz,e essa função conta e retorna quantas vezes esse número é encontrado na matriz"""
    soma = 0
    for i len(matriz):
        for j range(matriz[0]):
            if matriz[i][j] == numero:
                soma += 1
            else:
                soma
        return soma