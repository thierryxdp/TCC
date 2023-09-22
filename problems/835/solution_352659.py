def melhor_volta(matriz):
    
    dict_competidores = {}
    
    for i in range(len(matriz)):
        min_velue = min(matriz[i])
        index = matriz[i].index(min_velue)
        dict_competidores[i] = [min_velue, index]
        
	return dict_competidores