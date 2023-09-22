def melhor_volta(mat):
    
    #Melhor volta
    
    melhor_tempo = 0
    
    for index1 in range(len(mat)):
        melhor_volta = min(mat[index1])
        
        if melhor_tempo == 0:
            melhor_tempo = melhor_volta
        else:
            if melhor_volta < melhor_tempo:
                melhor_tempo = melhor_volta
                melhor_corredor = index1
    #Qual volta
    for index2 in range(10):
        volta = mat[melhor_corredor][index2]
        
        if volta == melhor_tempo:
            index2 += 1
            melhor_corredor += 1
            break
	return (melhor_corredor, melhor_tempo, index2)