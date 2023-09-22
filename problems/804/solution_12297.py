def filtra_pares (x, y, c, d):
    """recebe uma tupla com 4 elementos, todos inteiros, e retorna outra apenas com os elementos pares da original; tuple -> tuple"""
    if x%2 == 0:
      z=x
    else:
      z=None
    if y%2 == 0:
      a=y
    else:
      a=None
    if c%2 == 0:
      w=c
    else:
      c=None
    if d%2 == 0:
      q=d
    else:
      q=None
    return z, a, w, q