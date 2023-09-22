def primo(n):
    if n < 2:
        # 1 não é primo!
        return False
    
    for d in range(2,n):
        if n%d == 0:
            # se eu achei um divisor, o número NÃO é primo
            return False
	
    # se percorri todos e não encontrei divisor, então primo
    return True