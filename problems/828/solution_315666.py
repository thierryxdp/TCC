def primo(numero):
    if numero==2:
        return True
    for i in range(numero-1):
        if numero%(range(numero-1)[i+2])!=0:
            return True
        else:
        	return False