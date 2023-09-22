def primo(numero):
    divisores = 0
    for contador in numero:
        if numero%contador == 0:
            divisores = divisores + 1
	if divisores == 2:
        return True
    else:
        return False