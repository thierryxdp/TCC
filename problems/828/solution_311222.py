def primo(numero):
	'''Função que dado um número inteiro positivo, verifica se o mesmo é primo ou não.
	Entrada: int
	Saída: bool'''
    if numero < 2:
        return False
    else:
        for divisor in range(2, numero):
            if numero % divisor == 0:
               return False
        return True