def primo(n):
    for i in range(2, n):
        if not (n % i):
            return True
    return False