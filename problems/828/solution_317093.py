def primo(num):
    '''analisa e retorna se um número é primo ou não
    	int->bool'''
    
    divisores=0
    
    for i in range(2,numero):
        
        if num%i==0:
            
            divisores=divisores+1
            
        if divisores==0:
            return True
        
        else:
            return False