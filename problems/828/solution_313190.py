def primo(n):
    """função que dado um numero inteiro positivo, verifique se este numero é primo ou não"""
	contador = 0
	i = 0

	while i <= n or contador < 2:
    	i = i + 1    
		a = n % i
		if a == 0:
			contador = contador + 1
	

	if contador <= 2:
		return True
	else:

		return False