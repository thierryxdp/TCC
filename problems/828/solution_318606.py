def primo(n):
    """funcao para descobrir se o numero 'n' e primo"""
    n = int(input('digite um valor: '))
    for c in range(2, n):
        if n % c == 0:
            return n 'é primo'
        else:
            return n 'não é primo'