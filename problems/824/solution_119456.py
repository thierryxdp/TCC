def f(e):
  if e in ['a','e','i','o','u']:
    return e
  return e.upper

def mapeia(it,p):
  r=[]
  for e in it:
    r.append(p(e))
    
def uppCons(s):
  return mapeia(s,f)