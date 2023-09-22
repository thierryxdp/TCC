def primo(n):
    div=0
    for d in range(2,n):
        if n%d==0:
            div+=1
        else:
            div+=0
    if div==0:
        b=True
    else:
        b=False
    return b