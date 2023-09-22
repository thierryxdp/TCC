def filtra_pares (x, y, c, d):
    """recebe uma tupla com 4 elementos, todos inteiros, e retorna outra apenas com os elementos pares da original; tuple -> tuple"""
    if x%2 == 0:
      z=x
    else:
      z=()
    if y%2 == 0:
      a=y
    else:
      a=()
    if c%2 == 0:
      w=c
    else:
      c=()
    if d%2 == 0:
      q=d
    else:
      q=()
    return z, a, w, q