def colchao(medidas,H,L):
    ''' funcao que, dado os parametros de entrada, calcula se o tamanho do colchao passa pela porta 
        list[int,int,int],int,int --> bool '''
    
    x = medidas[1]
    y = medidas[2]
    
    if x=<L:
        return True
    
    elif x=<H:
        return True
    
    elif y=<L:
        return True
    
    elif y=<H:
        return True 
    
    else:
        return False