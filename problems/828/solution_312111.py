def primo(n):
    """essa funcao, dado um numero inteiro positivo n, 
	verifica se este numero é primo ou nao.
    int -> bool"""
    
    c = 0
    
    for x in range(1, n+1):
        if n % x == 0:
            c += 1
    
    if c == 2:
        return True
    
    else:
        return False