def conta_numero(numero, matriz):
    '''
    dados um número inteiro e uma matriz de números inteiros, retorna
    quantas vezes o número informado aparece na matriz

    int, array -> int
    '''

    elementos = []
    ocorrencias = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                       elementos.append(matriz[i][j])
    
    ocorrencias = elementos.count(numero)
    return ocorrencias