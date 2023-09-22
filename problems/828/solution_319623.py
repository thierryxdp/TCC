def primo(numero):

	contador = 0
    
	for elemento in range(2, numero):
		if numero % elemento == 0:
			contador += 1
            
	if numero < 0:
		return False
	else:
		return True