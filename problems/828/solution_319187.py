def primo(x):
    divisivel = 0
    for c in range (1, x+1):
        if x % c == 0:
            divisivel += 1
    if divisivel == 2:
        return True
    else:
        return False