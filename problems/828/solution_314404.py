def primo(x):
    '''verifica se o num e primo
    int -> bool'''
    
	if x >= 2:
        for y in range(2,x):
            if not(x%y):
                return False
    else:
		return False
    return True