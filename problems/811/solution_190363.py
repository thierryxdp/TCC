def colchao (medidas,H,L):

    #Área do colchao
	face1 = medidas[0] * medidas[1] 

	face2 = medidas[1] * medidas[2]

	face3 = medidas[0] * medidas[2]

    #Área da porta

    area_porta = H * L

	if (medidas[0] <= H or  medidas[0] <= L) and (medidas[1] <= H or medidas[1] <= L):
		return True
	if (medidas[1] <= H or  medidas[1] <= L) and (medidas[2] <= H or medidas[2] <= L):
		return True
	if (medidas[2] <= H or  medidas[2] <= L) and (medidas[0] <= H or medidas[0] <= L):
		return True
    
    else: 
	
		return False