def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    if n>1:
        for i in range (2,n):
            if n%i ==0:
                return False
            else:
                return True