def colchao(medidas,H,L): 
    '''
Função que recebe as medidas de um colchão  e de  uma porta
H, L  e retorna o booleano True caso passe e False caso contrário.

list ,int, int->bool
    '''
    
    if medidas[1]> max(H,L):
        return False 
    if medidas[0]> min(H,L):
        return False
    else:
        return True