def primo(n):
    c = 0
    for i in range (n):
        if n/i == 0:
            c = c + 1
    if c == 0:
        return True
    else:
        return False