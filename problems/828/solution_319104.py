def primo(x):
    for k in range(2,x):
        if x%k != 0:
            return True
    else:
    	return False