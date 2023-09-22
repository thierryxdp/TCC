def filtraMultiplos(ls,n):
    
def fm(x,n):
    if x%n==0:
      return True
    
    r = []
    for x in ls:
        if filtraMultiplos(x,n):
            r.append(x)
    return r