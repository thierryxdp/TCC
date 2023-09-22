def melhor_volta(matriz):
    lista_pelos_tempos = []
    lista_pelas_voltas = []
    
    for voltas in range(6):
        for tempos in range(10):
            if matriz[voltas][tempos] == min(matriz[voltas]):
                lista_pelos_tempos.append(tempos)