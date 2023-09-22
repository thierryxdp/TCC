def primo(n):
    """Função que diz se um numero é primo ou não
    int -> bool"""
    divisores = 0
    for c in range(1 , n+1):
        if n % c == 0:
            divisores = divisores + 1
    if divisores > 1:
        return False
    elif divisores < 3:
        return True
    else: 
         return True