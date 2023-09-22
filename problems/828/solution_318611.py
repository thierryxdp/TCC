def primo(n):
    """funcao para descobrir se o numero 'n' e primo"""
    for c in range(2, n):
        if n % c == 0:
            return ('\033[34m')
        else:
            return ('\033{m')