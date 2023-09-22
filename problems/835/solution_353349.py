def melhor_volta(matriz):
    '''função que dada uma matriz 6x10 retorna a linha
    do menor valor, o menor valor e a coluna do menor valor
    list -> tup
    '''
    melhor_tempo = volta = corredor = 1000
    for vencedor in range(len(matriz)):
        for tempo in range(len(matriz[vencedor])):
            if min(matriz[vencedor][tempo],melhor_tempo) == matriz[vencedor][tempo]:
                melhor_tempo = min(matriz[vencedor][tempo], melhor_tempo)
                corredor = vencedor +1
                volta = tempo + 1
    return corredor, melhor_tempo, volta