def primo(numero):
    i=2
    while i in range(numero):
        if numero%i == 0:
            i += 1
    		return 	False
        else:
            i += 1
   	return True