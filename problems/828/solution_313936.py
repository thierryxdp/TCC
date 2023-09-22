def primo(x):
    y = 0
    for n in range(2,x):
        if(x%n == 0):
            y += 1
    if y == 0:
        return True
    if y not == 0:
        return False