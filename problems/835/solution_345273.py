def melhor_volta(matriz):
    """dada uma matriz de tempos 6x10, onde cada linha representa um de seis corredores em uma pista de kart, e cada
    coluna representa os seus tempos em segundos em cada uma de dez voltas, a função retorna uma tupla informando qual
    entre os corredores teve a melhor volta, com qual tempo e em qual volta (assumindo que os corredores têm tempos
    diferentes). Os seis corredores são numerados de 1 a 6 e as voltas de 1 a 10; list -> tuple"""
    tempos_minimos = []
    volta = []

    for i in range(6):
        tempos_minimos += [min(matriz[i])]
        for j in range(10):
            if matriz[i][j] == min(matriz[i]):
                volta += [j]
                
    melhor_corredor = list.index(tempos_minimos, min(tempos_minimos))
    
    return (melhor_corredor + 1, min(tempos_minimos), volta[melhor_corredor] + 1)