def melhor_volta(matriz):
    tmps = []  
    vlts = [] 
    
    for corredor in range(1,7):  
        for voltas in range(1,11):  
            if matriz[corredor][voltas] == min(matriz[corredor]): 
                tmps = tmps + [voltas]  
    for i in range(1,7): 
        vlts = vlts + matriz[i][tmps[i]]
    volta = vlts.index(min(vlts))
    tempo = min(vlts)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, piloto)
    
    return tupla