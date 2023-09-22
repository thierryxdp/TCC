def primo(num):
    """
    	Retorna True se o número inserido for primo
        int -> bool
    """
    
    for i in range(2,num):
        if num%i==0:
            return False
    return True