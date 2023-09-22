def primo(numero):
    divisores = []
    for i in range(2,numero):
        if numero%i==0:
            divisores = divisores + [i,]
    if len(divisores) != 1:
    	return False
    else:
        return True