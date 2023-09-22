def primo(numero):		
    divisores=0
	for i in range(1,numero+1):
		if numero%i==0:
			divisores+=1       	       
           	return divisores<=2True
	else:
		return False