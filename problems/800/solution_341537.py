def total(l,p):
    r=[p[i] for i in l if i in p]
    return round(sum(r),2)