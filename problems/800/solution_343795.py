def  total(l,d):
    t=0
    for compras in l:
        t+=d[compras]
    round(t,2)        
    return t