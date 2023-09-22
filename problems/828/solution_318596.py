def primo(n):
	if n > 1:
    	for i in range(0, n):
        	if n % i == 0:
            	return False
    		else:
        		return True