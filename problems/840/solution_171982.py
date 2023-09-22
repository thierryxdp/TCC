def bolos(a, b, c):
  a = a//2
  b = b//3
  c = c//5
  if a<b and a<c:
    return a
  elif b<a and b<c:
    return b
  elif c<a and c<b:
    return c
  else:
    return a