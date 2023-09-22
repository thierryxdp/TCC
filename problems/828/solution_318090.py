def primo(n):
    ls=range(1, n+1)
    r=[]
    for x in len(ls):
        if n%ls[x]==0:
            r.append(ls[x])
    return len(r)==2