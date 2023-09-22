def primo(x):
    mult = 0
    for e in range(2, x):
        if (x%e==0):
            mult = mult + 1
    if (mult==0):
        return 'true'
    else:
        return 'false'