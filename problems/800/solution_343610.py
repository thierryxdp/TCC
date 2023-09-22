def total(l,d):
    tot=0
    for elementos in l:
        tot+=d[elementos]
    return round(tot,2)