def colchao(medidas,H,L): 
    '''
Função que recebe as medidas de um colchão  e de  uma porta
H, L  e retorna o booleano True caso passe e False caso contrário.
list ,int, int->boll
    '''
    if medidas[1]>=H and medidas[2]>=L  or medidas[1]<=L and medidas[2]>=medidas[1] or medidas[0]>=L:
       return False
 
    
    else:
       return True