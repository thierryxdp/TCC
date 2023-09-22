def primo(n):
	'''Verifica se o número (n) é ou nao um número primo;
		int --> bool'''
    s = 0
    for c in range(1, n+1):
        if n % c == 0:
        	s += 1
    if s == 2:
        return True
    else:
        return False