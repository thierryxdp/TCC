def primo(n):
    """Dado um número inteiro positivo retorna se este número é primo ou não
    int -> bool"""
    r = []
    for i in range(n+1):
        if i != 0:
        	if n%i == 0:
            	r.append(i)
    if len(r) == 2:
        return True
    else:
        return False