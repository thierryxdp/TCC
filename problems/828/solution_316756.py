def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    if n>2:
        for i in range (2,n+1):
            if n%i ==0:
                return False
            if n%2 == 0:
                return False
            if n%i != 0:
                return True
            if p % 2 != 0:
                return True