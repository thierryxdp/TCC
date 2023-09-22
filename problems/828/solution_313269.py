def primo(numero):			
	'''retorna se um numedo dado e primo
    int->bool'''
    divi=0
    for i in range(1,numero+1):		
        if numero%i==0:
			divi+=1 
	if divi<=2:
		return True
	else:
		return False