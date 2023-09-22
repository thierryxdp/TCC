def filtra_pares(x):
    if x[3] % 2 == 0:
     a = (x[3],)
    else:
      a = ()
    if x[2] % 2 == 0:
     b = (x[2],)
    else:
     b = ()
    if x[1] % 2 == 0:
     c = (x[1],)
    else:
     c = ()
    if x[0] % 2 == 0:
     d = (x[0],)
    else:
     d = ()
     return a + b + c + d