def primo(x):
    primoo = True
    for y in range(1, int(x / 2)):
        if(x % y == 0):
            primoo = False
    return primoo