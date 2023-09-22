def inverte(x):
  y = x.replace("."," ")
  p = y.replace(","," ")
  o = p.replace("!"," ")
  k = o.replace("?"," ")
  d = k.replace(":"," ")
  k1 = d.replace("-"," ")
  k2= k1.replace(";"," ")
  k3=str.split(k2)
  list.reverse(k3)
  espaco = " "
  k4 = str.lower(str.join(espaco,k3))
  return k4