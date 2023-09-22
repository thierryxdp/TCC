def primo(x):
    pp=[2,3,7,11,13,17,19]
    l=[]
    c=0
    for e in pp:
        if x%e==0:
            c=c+1
    return c==7