def conta_numero(n, mat):
  c = 0
  for lin in mat:
    for col in lin:
      if n == col:
        c = c + 1
  return c