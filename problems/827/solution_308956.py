def qtd_divisores(numero):
    '''analisa e retorna quantos divisores o numero possui
    	int->int'''
    
    divisores=[]
    
    for i in range(numero):
        
        if numero//i==0:
            
            divisores=divisores+i
    
    return divisores