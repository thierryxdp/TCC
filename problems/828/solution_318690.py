def primo(x):
    d=0
    e=range(2,x)
    for i in e:
        if x%i!=0:
            d=0
        else:
            d=d+1
    if d==0:
        return True
    else:
        return False