def primo(numero):
    if numero == 0:
        return False
    else:
        cont = 0
        for i in range(1, abs(numero) + 1):
            if numero%i == 0:
                cont += 1
		if cont > 2:
            return False
        return True