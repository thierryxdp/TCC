def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    for i in range (2,n+1):
        if n == 2 or n!= 1 or n%i == 0 or n%2 == 0:
            return False
        else:
            return True