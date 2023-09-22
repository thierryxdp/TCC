def colchao(medidas,H,L): 
    '''
Função que recebe as medidas de um colchão  e de  uma porta
H, L  e retorna o booleano True caso passe e False caso contrário.
list ,int, int->boll
    '''
    if medidas[0]<=H and medidas[1]<=L or medidas[2]<=H and L and medidas[2]<=H or medidas[0]<=L and medidas[1]<=medidas[0] or medidas[1]>=L:
       return True
    
    
    else:
       return False