def filtra_pares(x):
    if x[0] % 2 == 0:
     a = (x[0],)
    else:
      a = ()
    if x[1] % 2 == 0:
     b = (x[1],)
    else:
     b = ()
    if x[2] % 2 == 0:
     c = (x[2],)
    else:
     c = ()
    if x[3] % 2 == 0:
     d = (x[3],)
    else:
     d = ()
    if x[4] % 2 == 0:
     e = (x[4],)
    else :
     e = ()
     return a + b + c + d + e