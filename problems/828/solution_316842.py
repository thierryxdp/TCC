def primo(x):
    numPrimos = 0
    for contador in range(1, x + 1):
        if x % contador == 0:
            numPrimos += 1

    if numPrimos == 2:
        return True

    else:
        return False