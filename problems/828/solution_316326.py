def primo(n):
    divisor = 2
    for i in range(1, n):
        if n % i == 0:
            divisor = divisor + 1
            if divisor > 1:
                break
    if divisor == 1 and n>1:
        return "é primo"
    else:
        return "não é primo"