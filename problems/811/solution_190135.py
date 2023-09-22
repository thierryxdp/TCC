def colchao (medidas,H,L):

    #Área do colchao
    area_colchao =  2*medidas[0]*medidas[1] + 2*medidas[1]*medidas[2] + 2*medidas[0]*medidas[2]

    #Área da porta

    area_porta = H * L

    if  area_porta < area_colchao:
        return False

    if area_porta == area_colchao:
        return False

    if area_colchao > area_porta:
        return True