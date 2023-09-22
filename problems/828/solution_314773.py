def primo(n):
    """Função que dado um número inteiro, retorne se True se for primo,
    e False caso não.
    int -> bool"""
    
    for y in range(1, n+1):
        if y > 1 :
            if n%y == 0 and y != n:
                return False
    return True