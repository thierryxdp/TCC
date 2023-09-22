def primo(x):
    for k in range(2,x+1):
        if x%k == 0:
                return False
        else:
        	if x%k > 0:
           		return True