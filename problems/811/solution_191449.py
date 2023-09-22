def colchao(medidas, H, L):
    
    """ Dadas as 3 medidas de um colchao(lista), a 
    altura(int) e a largura(int) da porta de Joao, 
    a funcao retorna True se o colchao passa e 
    False caso contrario"""
    
    m = medidas
    
    if m[1] > L and m[1] > H and  m[2] > L and m[2] > H:
        
        return False
       
        
    
    else: 
        return True