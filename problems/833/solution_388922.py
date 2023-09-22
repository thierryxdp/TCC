def conta_numero(numero,matriz):
    '''Recebe um número inteiro e uma matriz contendo números inteiros
    e retorna quantas vezes o número aparece na matriz 
    (int, list -> int)'''
    contador = 0
    for i in matriz:
        for j in matriz[i]:
            if matriz[i][j] == numero:
                contador = contador + 1
        return contador