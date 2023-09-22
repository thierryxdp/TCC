def conta_numero(numero,matriz):
    '''funcao que, dado um numero e uma matriz de inteiros qualquer, retorna
    quantas vezes o numero aparece na matriz.
    int, matriz -> int'''
    frequencia = 0
    for i in range(len(matriz)):
        for j in matriz[i] :
            if j == numero:
                frequencia+=1
    return frequencia