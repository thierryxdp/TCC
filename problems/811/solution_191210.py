def colchao(medidas,H,L):
    
    '''A função verificará se um colção será capaz de passar por um porta.
    Insira as medidas, em centímetro, do colção na lista [medidas] e a altura (H) e a
    largura da porta (L) também em centímetros.
    
    Dados de entrada -> list, float, float
    Dados de saída -> Boolean'''
    
    A = medidas[25] 
    B = medidas[120] 
    C = medidas[220]
    
    if A <= L and B <= 	H or B <= L and A <= H:
        return True
    
    else:
        return False