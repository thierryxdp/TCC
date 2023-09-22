def primo(x):
    if x<2:
        for y in range(2,x-1):
            if (x%y):
                return True
    else:
        return False