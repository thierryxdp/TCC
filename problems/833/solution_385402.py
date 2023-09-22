def conta_numero(numero,matriz):
    """Função que, dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, retorna quantas vezes aquele número aparece na matriz
    entrada: int, list
    saída: int"""
    qntd_vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero
            qntd_vezes=qntd_vezes+1
    return qntd_vezes