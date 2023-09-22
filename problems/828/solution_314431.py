def primo(numero:int)->bool:
    teto = round(numero**(1/2))
    for i in range(1, teto + 1):
        if numero % i == 0:
            return False
	return True