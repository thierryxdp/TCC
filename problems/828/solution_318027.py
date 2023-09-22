def primo(n):
    return len(filtra(range(1,n+1),lambda x: x%n==0))==2
def filtra(ls,p):
    r=[]
    for e in ls:
        if p(e):
            r.append(e)