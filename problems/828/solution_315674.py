def primo(numero):
    if numero==2:
        return True
    else:
    	for i in range(numero+(-1)):
        	if numero%(i+1)!=0:
            	return True
        	else:
        		return False