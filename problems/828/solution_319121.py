def primo(x):
    for num in range(2,x):
        if (x%num) == 0:
            return False
        else:
            return True