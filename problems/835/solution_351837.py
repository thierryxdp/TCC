def melhor_volta(matriz):
    tmps = []  
    vlts = [] 
    
    for voltas in range(6): ## 6 corredores
        for tempos in range(10):  ###10 voltas
            if matriz[voltas][tempos] == min(matriz[voltas]): 
                tmps.append(tempos)  
    for i in range(6): 
        vlts.append(matriz[i][tmps[i]])
    volta = vlts.index(min(vlts))
    tempo = min(vlts)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, piloto)
    
    return tupla