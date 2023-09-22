def filtra_pares([a,b,c,d]):
    t = (a,b,c,d)
    if type(t)==tuple and len(t) == 4:
     for i in t:
       if i%2==0:
    
        return (tuple(i%2==0))