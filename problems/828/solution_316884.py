def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    if n==2:
        return True
    for i in range (3,n+1):
        if n%i == 0 or n%2 == 0 or n<2 :
            return False
        else:
            return True