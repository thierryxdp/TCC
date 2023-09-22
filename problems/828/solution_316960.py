def primo(n):
    for i in range(1,n):
        if n%i==0 and i!=n and i!=1:
            return False
        else:
            return True