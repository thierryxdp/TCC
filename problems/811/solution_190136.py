def colchao (medidas,H,L):

    #Área do colchao
    area_colchao =  medidas [0] * medidas [1] 

    #Área da porta

    area_porta = H * L

    if  area_porta < area_colchao:
        return False

    if area_porta == area_colchao:
        return False

    if area_colchao > area_porta:
        return True