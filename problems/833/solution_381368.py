def conta_numero(numero,matriz):
    '''conta_numero recebe uma numero e uma matriz e devolve a quantidade de vezes que o número aparece na matriz.
    float,list-->int.'''
    contador=0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if numero==matriz[linha][coluna]:
                contador=contador+1
    return contador