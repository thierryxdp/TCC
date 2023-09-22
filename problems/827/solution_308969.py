def qtd_divisores(numero):
    '''analisa e retorna quantos divisores o numero possui
    	int->int'''
    
    divisores=0
    
    for i in range(1,numero):
        
        if numero//i==0:
            
            divisores=divisores+1
        
        else:
            divisores=divisores+0
    
    return divisores