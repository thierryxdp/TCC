def primo(numero):
    divisores = []
    for i in range(1,numero):
        if numero%i==0:
            divisores = divisores + [i,]
    if len(divisores) != 2:
    	return False
    else:
        return True