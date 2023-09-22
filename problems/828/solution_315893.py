def primo(numero):
    """retorna se o número é primo ou não
    int->bool"""
    
    for d in range(1,numero):
    	if numero%d == 0:
            return True
        else:
            return False