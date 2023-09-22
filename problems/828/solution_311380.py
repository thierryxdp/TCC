def primo(x):
    pp=[2,3,7,11,13,17,19,71]
    l=[]
    c=0
    if x in pp:
        return 2==2
    else:
        for e in pp:
            if x%e==0:
                c=c+1
        return not c>0