def primo(n):
    t=1
    s=0
    while s<3:
        if n//t==0:
            s+=1
            t+=1
        else:
            t+=1
        return s<3