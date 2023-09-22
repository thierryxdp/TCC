def colchao(medidas,H,L):
    ''' funcao que, dado os parametros de entrada, calcula se o tamanho do colchao passa pela porta 
        list[int,int,int],int,int --> bool '''
    
    x = medidas[1]
    y = medidas[2]
    
    if H*L >== (x)*(y):
        return True
    
    else:
        return False