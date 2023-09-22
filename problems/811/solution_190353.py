def colchao (medidas,H,L):

    #Área do colchao
	face1 =  medidas[0]* medidas[1]

	face2 =  medidas[1]* medidas[2]

	face3 =  medidas[0]* medidas[2]

    #Área da porta

    area_porta = H * L

	if face1 < area_porta or face2 < area_porta or face3 < area_porta

        return False

    else: 
	
		return True