def primo(n: int) -> bool:
    """Essa função, dado um número inteiro,
    determina se é primo (True) ou não (False)."""
    
    zeros = 0
    
    for i in list(range(1, n+1)):
        if n % i == 0:
            zeros += 1
    
    if zeros == 2:
        return True
    else:
        return False