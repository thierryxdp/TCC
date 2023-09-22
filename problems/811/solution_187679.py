def colchao(medidas,H,L): 
    '''
Função que recebe as medidas de um colchão  e de  uma porta
H, L  e retorna o booleano True caso passe e False caso contrário.
list ,int, int->boll
    '''
    if (L <= medidas[0]and medidas[1], medidas[2] <= H ) or (L <= H or H <=L):   
       return True
 
    else:
       return False