def primo(n):
    """funcao para descobrir se o numero 'n' e primo"""
    for c in range(2, n):
        if n % c == 0:
            return n 'e primo'
        else:
            return n 'nao e primo'