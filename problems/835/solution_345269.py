def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 com os tempos (em segundos) das 10 voltas de
    6 corredores (cada linha representa todos os tempos de um corredor, e
    cada coluna os tempos de todos os corredores em uma das voltas).

    Retorna uma tupla contendo: De quem foi a melhor volta da prova, com
    qual tempo e em que volta.

    obs: os corredores têm tempos diferentes
    obs2: os corredores são representados por números de 1 a 6 e as voltas
    por números de 1 a 10
    
    list -> tuple '''

    numLinhas = 6
    numColunas = 10
    
    temposMin = []

    for i in range(numLinhas):
        tempoMinCorredor = min(matriz[i])
        list.append(temposMin, tempoMinCorredor)

    melhorTempo = min(temposMin)
    quemMelhorVolta = list.index(temposMin, melhorTempo) + 1
    qualVolta = list.index(matriz[quemMelhorVolta-1], melhorTempo) + 1

    return (quemMelhorVolta, melhorTempo, qualVolta)