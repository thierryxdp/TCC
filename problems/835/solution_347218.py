def melhor_volta(matriz):
    participante = 0
    menor = matriz[0][0]
    volta = 0
	for i in range(0,6):
        
        for j in matriz[i]:
            if j <= menor:
                menor = j
                participante = i+1
    		
            if j != 1:
                volta += 1
            else:
            	volta =1
    
    resultado = (participante,menor,volta)
    return resultado