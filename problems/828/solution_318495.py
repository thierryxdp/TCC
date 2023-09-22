def primo(n):
    x=0
    for v in range(n):
        if n%(v+1)==0:
            x+=1
    if x==2:
        return True
    else:
        return False