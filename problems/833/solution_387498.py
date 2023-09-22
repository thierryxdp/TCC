def conta_numero(numero,matriz):
    '''Função que dado um numero inteiro e uma
    matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele número
    aparece na matriz.int,matriz->int'''
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                total=total+1
    return total