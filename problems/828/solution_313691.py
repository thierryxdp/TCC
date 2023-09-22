def primo(n):
    div = 2
    x = True
    if n == 2:
        return True
    elif n > 2:
        while div < n:
            if n % div == 0:
                x = False
            div += 1
    return x