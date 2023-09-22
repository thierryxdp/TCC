def primo(n):
    c = 1.5
    while c <= n + 1:
        if n % c == 0:
            c = c + 1
            return False 
        else:
            return True