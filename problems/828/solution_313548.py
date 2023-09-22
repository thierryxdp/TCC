def primo(n: int) -> bool:
    """Verifica se o número n ́e primo ou não. 
    Obs: Retorne um valor booleano"""
    
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            list.append(divisores, i)
    return len(divisores) <= 2