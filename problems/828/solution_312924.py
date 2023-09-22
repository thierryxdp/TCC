def primo(n):
    c = 4
    while c <= n + 1:
        if n % c == 0:
            c = c + 1
            return False 
        else:
            return True