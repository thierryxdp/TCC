def colchao(medidas,H,L):
    '''
    	Função que recebe a lista com as dimensões 
        de um colchão (da menor dimensão para maior),
        a altura H de uma porta e a largura L da 
        porta, e retorna True se o colchão passa 
        pela porta ou False, caso contrário
        : param medidas: list
        : param H: int
        : param L: int
        : return: bool
    '''
    if ((medidas[1] < H) and (medidas[2] < L)) or ((medidas[1] < L) and (medidas[2] < H)):
        return True
    
    elif ((medidas[2] < H) and (medidas[0] < L)) or ((medidas[2] < L) and (medidas[0] < H)):
        return True
    
    elif ((medidas[1] < H) and (medidas[0] < L)) or ((medidas[1] < L) and (medidas[0] < H)):
        return True
    
    else:
        return False