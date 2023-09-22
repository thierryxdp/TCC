def primo(n):
    c = -2
    while c <= n + 1:
        if n % c == 0:
            c = c + 1
            return False 
        else:
            return True