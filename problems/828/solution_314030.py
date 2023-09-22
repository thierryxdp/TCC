def primo(n):
    a=1
    b=False
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
            b=True
    return b