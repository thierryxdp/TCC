def primo(x):
    if x<=2:
        for y in range(2,x):
            if (x%y):
                return False
            return True
    else:
        return  False
    return True