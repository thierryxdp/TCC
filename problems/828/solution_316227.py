def primo(n):
    nprimos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nprimos += 1

    if nprimos == 2:
        return True
    else:
        return False