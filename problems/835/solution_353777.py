def melhor_volta(matriz):
    '''Retorna o corredor com a volta mais rápida assim como o tempo
    e a própria volta.
    list --> tuple'''
    
    melhorCorredor = 0
    melhorVolta = 0
    melhorTempo = matriz[0][1]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if melhorTempo > matriz[i][j]:
                melhorTempo = matriz[i][j]
                melhorVolta = j
                melhorCorredor = i
                
	return (melhorCorredor,melhorTempo,melhorVolta)