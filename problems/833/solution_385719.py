def conta_numero(numero,matriz):
    '''funcao que, dado um numero e uma matriz de inteiros qualquer, retorna
    quantas vezes o numero aparece na matriz.
    int, matriz -> int'''
    frequencia = 0
    for linha in range(len(matriz)):
        for n in linha:
            if n == numero:
                frequencia+=1
    return frequencia