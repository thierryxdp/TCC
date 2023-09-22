def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    if n%(n-1)!=0:
        return True