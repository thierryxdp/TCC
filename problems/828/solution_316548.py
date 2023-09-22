def primo(numero):

	"""Recebe um numero e retorna se é um numero primo
	ou não; int-> bool."""
    
	divisores=[]
    for i in range (2,numero):
        if numero % i == 0:
            divisores+=i	
            
    if divisores>0:
        
        return False
    
    else:
        
        return True