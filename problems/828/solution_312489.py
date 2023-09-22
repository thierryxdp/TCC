def primo(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return True
        else:
            return False