def primo(numero):
    ''' Dado um numero inteiro positivo, retorna 
    se ele é primo ou nao'''
    contador = 0
    for x in range(1, numero):
        if numero % x == 0:
            contador += 1
	if contador > 1:
        return False
    else:
        return True