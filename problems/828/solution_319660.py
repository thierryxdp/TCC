def primo(n):
    r=range(1,n+1)
    if len(filtra(r,lambdax: n%x==0))==2:
        return True
    else:
        return False
    
def filtra(ls,p):
    r=[]
    for e in ls:
        ifp(e):
            r.append(e)
    return r