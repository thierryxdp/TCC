def primo(numero):
    if numero==2:
        return True
    for i in range(numero):
        if numero%(i+2)!=0:
            return True
        else:
        	return False