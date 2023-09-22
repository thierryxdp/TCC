def melhor_volta(matriz):
    """Informa quem fez a melhor volta, em quanto tempo e em qual volta
       list --> tuple"""
    melhor_volta = matriz[0][0]
    corredor = 0
    volta = 0
    
    for i in matriz:
        for tempo_volta in i:
            if tempo_volta < melhor_volta:
                melhor_volta = tempo_volta
                corredor = matriz.index(i) + 1
                volta = i.index(tempo_volta) + 1
    return (corredor, melhor_volta, volta)