def primo(numero):
	'''Recebe um numero inteiro positivo
    e retorna True caso ele seja primo e
    false caso nao seja primo
    
    int -> bool
    '''
	
    contador = 0
	for elemento in range(2, numero):
		if numero % elemento == 0:
			contador += 1
	
    if contador > 0:
		return False
	
    else:
		return True