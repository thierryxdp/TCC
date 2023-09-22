def primo(x):
    if x<=2:
        for y in range(2,x):
            if not(x%y):
                return False
    else:
        return True
    return False