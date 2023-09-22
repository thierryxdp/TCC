def conta_numero (n,m):
    s= ()
    c=0
    for elem in m[c]:
        if elem == n:
            s +=1
        if c < len (m):
            c+=1
    return s