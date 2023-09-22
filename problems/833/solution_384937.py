def conta_numero(n,matriz):
    """Função que ao receber um número inteiro e uma matriz de números
    inteiros, retorna quantas ocorrências esse número tem na matriz;
    int, list -> int"""
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if n == matriz[i][j]:
                cont +=1
    return cont