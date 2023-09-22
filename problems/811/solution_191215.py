def colchao(medidas,H,L):
    '''A função verificará se um colção será capaz de passar por um porta.
    Insira as medidas, em centímetro, do colção na lista [medidas] e a altura (H) e a
    largura da porta (L) também em centímetros.
    
    Obs: A primeira medida da lista deve ser referente a altura do colchão,
    	 A segunda deve ser ferente a altura ou o comprimento
         A terceira deve ser ferente a altura ou o comprimento
         
   	Dados de entrada -> list, float, float
    Dados de saída -> Boolean'''
    
    
    A = medidas[0] #altura
    B = medidas[1] #largura ou comprimento
    C = medidas[2] #comprimento ou comprimento
    
    if A <= L and B <= 	H or B <= L and A <= H:
        return True
    
    else:
        return False