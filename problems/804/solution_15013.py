def filtra_pares(s):
    a = s[0] 
    b = s[1] 
    c = s[2]
    d = s[3]
    s = ()
    if a%2==0:
        s=s + (a,)
    if b%2==0:
		s=s + (b,)
    if c%2==0:
        s=s + (c,)
    if d%2==0:
        s=s + (d,)
    
    return s