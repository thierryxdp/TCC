def primo(n):
    return len(filtra(range(1, n + 1), lambda x: x % n == 0)) == 2