def colchao(medidas,H,L):
    '''explicação'''
    soma1 = 0
    soma2 = 0
    
    if H>L:
    	if H<medidas[0]:
        	soma1 = soma1 + 1
    	if H<medidas[1]:
        	soma1 = soma1 + 1
    	if H<medidas[2]:
        	soma1 = soma1 + 1
     
    if H<L:
        if L<medidas[0]:
        	soma2 = soma2 + 1
    	if L<medidas[1]:
        	soma2 = soma2 + 1
    	if L<medidas[2]:
        	soma2 = soma2 + 1 
            
    if soma1 and soma2 > 1
    	return False
    else:
        return True