def conta_numeros(numero,matriz):
    '''Dado um numero e uma matriz, respectivamente, a funcao retorna a
    quantidade de vezes que o numero dado aparece na matriz. o numero e
    os elementos da matriz devem ser inteiros.
    int, list -> int'''
    contador=0
    for i in range(matriz):
        for j in range(matriz[0]):
            if numero==matriz[i][j]:
                contador+=1
    return contador