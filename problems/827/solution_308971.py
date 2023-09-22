def qtd_divisores(numero):
    '''analisa e retorna quantos divisores o numero possui
    	int->int'''
    
    divisores=0
    
    for i in range(1,numero+1):
        
        if numero%i==0:
            
            divisores=divisores+1
        
        
    
    return divisores