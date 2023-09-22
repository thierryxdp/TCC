def colchao(medidas,H,L):
    ''' funcao que, dado os parametros de entrada, calcula se o tamanho do colchao passa pela porta 
        list[int,int,int],int,int --> bool '''
    
    x = medidas[1:2]
    y = medidas[2:]
    
    if x =< H:
        return True 
    
    elif x =< L:
        return True
    
    elif y =< H:
        return True 
    
    elif y =< L:
        return True
    
    else:
        return False