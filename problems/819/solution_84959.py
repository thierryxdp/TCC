def filtraMultiplos(ls,n):
    
    def fm(x,n):
       if x%n==0:
         return True
    
    r = []
    for n in ls:
        if filtraMultiplos(x,n):
            r.append(x)
    return r