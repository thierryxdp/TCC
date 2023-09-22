def primo(x):
    divisor = False
    for y in range(x / 2):
        if(x % y == 0) and (y > 1):
            divisor = True
    return divsor