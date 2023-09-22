def primo(num):
    for menor in list(range(2, num)):
        if num%menor == 0:
            return False
    return True