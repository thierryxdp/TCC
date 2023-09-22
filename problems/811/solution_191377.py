def colchao(medidas,H,L):
    ''' funcao que, dado os parametros de entrada, calcula se o tamanho do colchao passa pela porta 
        list[int,int,int],int,int --> bool '''
    
    if H*L >== medidas[1]*medidas[2]:
        return True
    
    else:
        return False