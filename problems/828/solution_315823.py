def primo(n):
    x=True
    for d in range(2,n):
        while x:
            if n % d == 0:
                return False
            else:
                return True