def primo(n):
    ls=range(1, n+1)
    r=[]
    x=0
    while x < len(ls):
        if n%ls[x] == 0:
            
            r=r+ls[x]
            x=x+1
    return len(r)==2