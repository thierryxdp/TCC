def primo(n):
    x = n
    c = 0
    while x >=1:
        if n%x == 0:
            c+=1
        x -=1
    if c == 2:
        return True
    else:
        return False