def melhor_volta(matriz):
    participante = 0
    menor = matriz[0][0]
	for i in range(0,6):
        for j in matriz[i]:
            if j <= menor:
                menor = j
                participante = i
                j += 1
            else:
                j += 1
       	 
    
    resultado = (participante,menor,i)
    return resultado