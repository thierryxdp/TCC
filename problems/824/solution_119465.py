def f(e):
  if e in ['a','e','i','o','u']:
    return e
  return e.upper

def mapeia(s,f):
  r =[]
  for e in s:
    r.append(f(e))
  return r
    
def uppCons(s):
  return str.join(mapeia(s,f))