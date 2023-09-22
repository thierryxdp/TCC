def primo(n):
    for numero in range(1,n+1):
        if n == 2:
            return True
        if n%2!= 0:
            return True
        else:
            return False