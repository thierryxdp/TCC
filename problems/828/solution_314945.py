def primo(n):
    c = 1
    for i in range (n):
        if n/i == 0:
            c = c + 1
    if c == 1:
        return True
    else:
        return False