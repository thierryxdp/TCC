def primo(x):
    p=range(2,x,1)
    for h in p:
        if x%h==0:
            return False
        else:
            return True