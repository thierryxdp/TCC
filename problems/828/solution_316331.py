def primo(n):
    """Função que dado um int verifica se este némero é primo.
    int -> bool."""
    divisor = 0
    for i in range(1, n):
        if n % i == 0:
            divisor = divisor + 1
            if divisor > 1:
                break
    if divisor == 1 and n>1:
        return "True"
    else:
        return "False"