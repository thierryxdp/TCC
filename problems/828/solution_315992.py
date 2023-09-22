def primo(x):
    divisor = False
    for y in range(2, int(x / 2)):
        if(x % y == 0):
            divisor = True
    return !divisor