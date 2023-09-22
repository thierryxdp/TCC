def primo(numero):
   	divisores=0
	if divisores<=2:
   
    	for i in range(1,numero+1):
        	if numero%i==0:
    				divisores+=1
    	return True
   	 else:
        return False