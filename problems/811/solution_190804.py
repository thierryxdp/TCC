def colchao(medidas,H,L):
    '''Analisa se é possível ou não a passagem do colchão pela porta
    	list,int,int->bool'''
    
    if medidas[1]<=L:
        return True
    else:
        if medidas[1]<=H:
            return True
        else:
            return False