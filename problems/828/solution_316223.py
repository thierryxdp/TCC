def primo(n):
    p = [2,3,5,7,11,13,19,23,29]
    while n in p:
        return True
    while n not in p:
        if n % n**(1/2) == 0:
            return False
        if n % 3 == 0:
            return False
        if n % 5 == 0:
            return False
        if n % 7 == 0:
            return False
        if n % 11 == 0:
            return False
        if n % 13 == 0:
            return False
        else:
            return True