def mapeia(ls, f):
  r = []
  for e in ls:
    r.append(f(e))
  return r

def lingua_p(s):
  def f(x):
    if x in ("a","e","i","o","u"):
      return x + "p" + x
    else:
      return x
  return "".join(mapeia(s, f))