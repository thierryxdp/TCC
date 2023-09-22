def primo(n):
    if (n <= 3):
        return True
    if (n<=1 or n % 2 == 0 or n % 3 ==0):
        return False
    else:
        return True