def melhor_volta(Matriz):
    ContadorColuna = 0
    ContadorLinha = 0
    Menor = min(Matriz[0])
    for Linhas in Matriz:
        ContadorColuna = 0
        ContadorLinha +=1
        if Menor in Linhas:   
        	for Coluna in Linhas:
            	ContadorColuna += 1
        		if Menor == Coluna:
               		return (ContadorLinha, Menor, ContadorColuna)