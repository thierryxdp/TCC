def conta_numero (numero, matriz):
    '''A função tem como parametro de entrada um numero inteiro e uma matriz de inteiros,
        retornando a quantidade de vezes que o numero aparece na matriz.
        int, list --> int
    '''
    contagem = []
    i = 0
    for elem in  matriz:
        for elem in matriz[i]:
            if elem == numero :
                list.append(contagem, numero)
        i+=1
    return len(contagem)