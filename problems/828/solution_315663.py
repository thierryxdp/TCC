def primo(numero):
    if numero==2:
        return True
    for i in range(numero):
        if numero%range(numero-1)[i+1]!=0:
            return True
        else:
        	return False