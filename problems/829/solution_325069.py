def mapeia(ls,x):
    r=[]
    
    for e in ls:
        r.append(x(e))
    return r

def soma_h(x):
    r = range(1,x+1)
    
    return round(sum(mapeia(r,lambda y: 1/y)),2)