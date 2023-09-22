def primo(n):
    i=1
    x=0
    while i<=n:
        if n%i==0:
            x+=1
        i+=1
    return true if x==2