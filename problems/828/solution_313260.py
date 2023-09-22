def primo(numero):		
	divi=0
	for i in range(1,numero+1):
		if numero%i==0:
			divi=divi + 1  
	return divi
   	else:
		return False