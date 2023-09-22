def primo(n):
    """Recebe um número e retorna se ele é primo ou não.
    int -> boolean"""
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        if count > 2:
            return False
    return True