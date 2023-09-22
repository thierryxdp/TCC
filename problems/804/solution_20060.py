def filtra_pares(a,b,c,d):
   if a%2 == 0:
    return a
   if b%2 == 0:
    return b
   if c%2 == 0:
    return c
   if d%2 == 0:
    return d
   if a%2 == 0 and b%2 == 0:
    return a,b
   if a%2 == 0:
    return a
   if a%2 == 0 and c%2 == 0:
    return a,c
   if b%2 == 0 and c%2 == 0:
    return b,c
   if a%2 == 0 and b%2 == 0 and c%2 == 0:
    return a,b,c