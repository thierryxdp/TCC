def primo(x):
    divisores = 0
    for divisor in list(range(2,x+1)):
        resto = x%divisor
        if resto == 0 and divisor!=x:
            return False
	return True