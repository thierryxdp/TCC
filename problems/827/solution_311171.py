def filtra(ls,p):
    r=[]
    
    for e in ls:
        if p(e):
            r.append(e)
    return r

def qtd_divisores(x):
    r = range(1,x+1)
    
    return len(filtra(r,lambda y:x%y == 0))