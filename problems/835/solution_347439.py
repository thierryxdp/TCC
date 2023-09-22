def melhor_volta(matriz):
    """Função que recebe uma matriz 6x10 com os tempos em segundos de cada volta de um corredor. Retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta.
    list -> tuple """

    melhor_tempo = 999999

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if min(matriz[i]) < melhor_tempo:
                melhor_tempo = min(matriz[i])
                corredor = i + 1
                volta = list.index(matriz[i], melhor_tempo) + 1


    return (corredor, melhor_tempo, volta)