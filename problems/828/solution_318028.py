def primo(n):
    ls = range(1,n+1)
    return len(filtra(ls,lambda x: x%n==0))==2
def filtra(ls,p):
    r=[]
    for e in ls:
        if p(e):
            r.append(e)