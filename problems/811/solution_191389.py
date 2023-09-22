def colchao(medidas,H,L):
    ''' funcao que, dado os parametros de entrada, calcula se o tamanho do colchao passa pela porta 
        list[int,int,int],int,int --> bool '''
    
    x = int(medidas[1])
    y = int(medidas[2])
    
    if H >= x:
        return True 
    
    elif L >= x:
        return True
    
    elif H >= y:
        return True 
    
    elif L >= y:
        return True
    
    else:
        return False