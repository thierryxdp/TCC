def qtd_divisores(numero):
    '''analisa e retorna quantos divisores o numero possui
    	int->int'''
    
    divisores=[]
    
    for i in range(1,numero):
        
        if numero//i==0:
            
            divisores.append(i)
    
    return divisores