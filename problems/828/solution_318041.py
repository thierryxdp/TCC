def primo(n):
    ls = range(1,n+1)
    a = filtra(ls,lambda x: x%n==0)
    return len(a)==2
def filtra(ls,p):
    r=[]
    for e in ls:
        if p(e):
            r.append(e)