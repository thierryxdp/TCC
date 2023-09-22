def primo(numero):
    """retorna se o número é primo ou não
    int->bool"""
    
    for divisor in range(2,numero):
    	if numero%divisor == 0:
            return False
    return True