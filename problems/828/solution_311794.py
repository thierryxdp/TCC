def primo(n):
    """Essa função verifica se um numero(n) é primo"""
    """int->bool"""
	p=0
	for i in range(1,n+1):
		if ((n%i) == 0):
			p=p+1
	if p>2:
		return False
	return True