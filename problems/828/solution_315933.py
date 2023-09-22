def primo(n):
    l=list(range(1,n))
    r=[+1 for i in l if n%i==0]
    if r<2:
        return True
    else:
        return False