def filtra_pares(a,b,c,d):
 x=()
 if a&2 == 0:
    x=x+(a,)
 if b&2 == 0:
    x=x+(b,)
 if c&2 == 0:
    x=x+(c,)
 if d&2 == 0:
    x=x+(d,)
 return x