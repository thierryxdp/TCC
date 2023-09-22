def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    if n==2:
        return True
    for i in range (3, n+1):
        if n%3 == 0 or n%2==0 or n<2 or n%4 == 0 or n%5 == 0 or n%6 == 0 or n%7 == 0
        or n%8 == 0 or n%9 == 0:
            return False
        else:
            return True