def primo(n):
    """Retorna um valor booleano ao verificar se um numero é primo ou nao, dado:
    um numero inteiro positivo"""

    if n<=1:
        return False
    elif n==2:
        return True
    for i in range (2,n):
        if n%i==0
            return False
    return True