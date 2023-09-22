def primo(n):
    while n not in p:
        if n % n**(1/2) == 0:
            return False
        else:
            return True