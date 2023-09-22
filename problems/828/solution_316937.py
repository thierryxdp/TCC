def primo(n):
    '''Retorna se um numero n é primo ou não
    	int -> bool'''
    for i in range(2, n):
        if n%i == 0:
            return False
	return True