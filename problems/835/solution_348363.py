def melhor_volta(matriz: list)-> tuple:
    
    tempos = []
    voltas = []
    for tempo in range(1,7):
        list.append(tempos, min(tempo))
        for volta in range(1,11):
            volta = list.index(min(tempo)) + 1
            list.append(voltas,volta)
    corredor = list.index(min(tempos)) + 1
    volta_min = voltas[corredor - 1]
                           
    return (corredor,min(tempos),volta_min)