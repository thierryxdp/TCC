def primo(n):
    x = 2
    while n % x != 0 and x < n/2:
        x = x + 1
    if n % x == 0:
        return False
    else:
        return True