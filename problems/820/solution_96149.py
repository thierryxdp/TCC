def primo(n):
    if n%2 == 0:
        return False
    else:
        for i in range(3,n+1):
            if n%i == 0:
                return False
        return True