def primo(x):
    primoo = True
    for y in range(1, x):
        if(x % y == 0) and (y > 1):
            primoo = False
    return primoo