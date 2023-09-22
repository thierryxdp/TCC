def primo(n):
    y=range(1,n)
    for d in y:
        if n%d==0 and n>d>1:
            b=False
        if n%d!=0 and n>d>1:
            b=False
        else:
            b=True
    return b