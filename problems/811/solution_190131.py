def colchao (medidas,H,L):

    #Área do colchao

    area_colchao =  2*a*b + 2*bc + 2*a*c

    #Área da porta

    area_porta = H * L

    if  area_porta > area_colchao:
        return True

    else :
        return False