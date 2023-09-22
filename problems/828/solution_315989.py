def primo(x):
    divisor = False
    for y in range(int(x / 2)):
        if(x % y == 0) and (y > 1):
            divisor = True
    return divsor