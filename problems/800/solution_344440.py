def total(x,y):
    t=0
    for i in x:
        t=t+dict.get(y,i,0)
    return round(t,2)