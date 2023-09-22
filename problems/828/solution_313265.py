def primo(numero):			
	for i in range(1,numero+1):
		divi=0
        if numero%i==0:
			divi+=1 
			return divi<=2
	else:
		return False