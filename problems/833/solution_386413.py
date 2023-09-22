def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho qualquer, 
    conta e retorna quantas vezes aquele número aparece na matriz.
    int,list->int
    '''
    qtd=0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if numero==matriz[x][y]:
                qtd+=1
    return qtd