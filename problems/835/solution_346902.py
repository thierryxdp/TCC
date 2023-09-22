def melhor_volta(matriz):
    tempos = []
	
    for i in matriz:
        for j in i:
            tempos.append(j)
    
    cont = 0
    while min(tempos) not in matriz[contador]:
        contador += 1
    corredor = contador + 1
    n_volta = matriz[contador].index(min(tempo)) +1
    
    return ganhador, min(tempo), n_volta