def filtra_pares(l):
    a, b, c, d = l
    l1 = ()
    if a % 2 == 0:
        l1 = l1 + (a,)  
    if b % 2 == 0:
        l1 = l1 + (b,)
    if c % 2 == 0:
        l1 = l1 + (c,) 
    if d % 2 == 0:
        l1 = l1 + (d,)
    else l1 = l1
        return l1