def primo(n):
    """Esta é a função  que dado um número inteiro positivo retorna se ele é primo ou não, int -> bool"""
    i=0
    
    for x in range(2,n):
        
        if (n % x == 0):
         i = i + 1

    if(i==0):
        
        return True

    else:
        return False