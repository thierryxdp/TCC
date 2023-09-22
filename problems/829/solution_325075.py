def soma_h(n):
    r= range(1,n+1)
    return round(sum(mapeia(r,lambda x: 1/x)),2)

def mapeia(ls,f):
    r=[]
    for e in ls:
        r.append(f(e))
    return r