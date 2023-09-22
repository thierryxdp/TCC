def melhor_volta(matriz):
    tmps = []  ## lista de tempos
    vlts = []  ## lista de voltas
    
    for voltas in range(6): ## 6 corredores
        for tempos in range(10):  ###10 voltas
            if matriz[voltas][tempos] == min(matriz[voltas]): 
                tmps.append(tempos)  
    for i in range(6): 
        vlts.append(matriz[i][tmps[i]])
    volta = vlts.index(min(vlts)) ## o indice
    tempo = min(vlts) ## o menor
    piloto = matriz[volta].index(tempo)+1
    
    retorno = (volta+1, tempo, piloto)
    
    return retorno