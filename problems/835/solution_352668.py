def melhor_volta(matriz):
    
    tuple_resultado = (0, 0, 0)
    
    for i in range(len(matriz)):
        min_tempo = min(matriz[i])
        index_menor_volta = matriz[i].index(min_tempo)
        
        if tuple_resultado[1] < min_tempo:
            tuple_resultado = (i, min_tempo, index_menor_volta)
        
	return tuple_resultado