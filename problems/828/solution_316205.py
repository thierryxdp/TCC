def primo(n):
    c = 1
    c1 = 0
    while c <= n:
        if n % c == 0:
            c1 = c1 + 1
            c = c + 1
            if c1 == 2:
                return True
            else:
                return False