def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
     divisores = 0
        for i in range(1, n):
        if n % i == 0:
            divisores = divisores + 1
            if divisores > 1:
            return False
        else:
            return True