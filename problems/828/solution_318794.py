def primo(n):
    if n == 1:
        return false
    x = 0
    for r in range(2,n):
        if(n%r == 0):
            x += 1
    if x == 0:
        return True
    else:
        return False