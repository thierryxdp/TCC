def primo(x):
    p=range(1,x)
    for h in p:
        if x%h==0:
            return False
        else:
            return True