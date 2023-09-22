def primo(n):
    q = 0

    for i in [2, 3, 5, 7]:
        if n / i == int(n / i):
            return False

    for i in range(n)[1::2]:
        if n / i == int(n / i):
            q += 1

    return q == 1