def maiores(ln,n):
    ''''''
    list.sort(ln)
    if min(ln) < n:
        list.remove(ln,min(ln))
    if min(ln) < n:
        list.remove(ln,min(ln))
    if min(ln) < n:
        list.remove(ln,min(ln))    
    return ln