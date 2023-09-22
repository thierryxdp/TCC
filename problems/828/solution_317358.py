def primo(n):
    qtd = 0
    for c in rangee(1, n +1):
        if n % c == 0:
            qtd += 1
    return qtd <= 2