def primo(n):
    divisor = 0
    for i in range(1, n):
        if n % i == 0:
            divisor = divisor + 1
            if divisor > 1:
                break
    if divisor == 0 and n>1:
        return "True"
    else:
        return "False"