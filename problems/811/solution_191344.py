def colchao(medidas, H, L):
    [A,B,C] = medidas
    '''
    	funcao que recebe as medidas do colchao e 
        as medidas de uma porta e retorna se é possivel ou impossivelpassar pela mesma.
    '''
    
    result = bool
    if medidas[0]<=L and medidas[1]<=H:
        result = True
    elif medidas[1]<=L and medidas[0]<=H:
        result = True
    elif medidas[0]<=L and medidas[2]<=H:
    	result = True
    else:
        result = False
        
        return result