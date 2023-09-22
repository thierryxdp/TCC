def melhor_volta(matriz):
    participante = 0
    menor = matriz[0][0]
    volta = 0
    mvolta = 0
	for i in range(0,6):
        
        for j in matriz[i]:
            if j <= menor:
                menor = j
                participante = i+1
                mvolta = volta+1
            if volta != 10:
                volta += 1
            else:
            	volta = 1
    
    resultado = (participante,menor,mvolta)
    return resultado