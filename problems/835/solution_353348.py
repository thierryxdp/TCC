def melhor_volta(matriz):
    '''função que dada uma matriz 6x10 retorna a linha
    do menor valor, o menor valor e a coluna do menor valor
    list -> tup
    '''
    corredor = 0
    volta = 0
    for vencedor in range(len(matriz)):
        for tempo in range(len(matriz[vencedor])):
            if tempo == min(matriz[vencedor]):
                melhor_tempo = tempo
                corredor = vencedor + 1
                volta = tempo + 1
    return corredor, melhor_tempo, volta