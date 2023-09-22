def colchao (medidas,H,L):

    #Área do colchao

    area_colchao =  2*A*B + 2*BC + 2*A*C

    #Área da porta

    area_porta = H * L

    if  area_porta > area_colchao:
        return True

    else :
        return False