def primo(numero):
    divisores = 0
    for contador in range(1,numero+1):
        if numero%contador == 0:
            divisores = divisores + 1
	if divisores == 2:
        return True
    else:
        return False