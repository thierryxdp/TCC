def inverte(frase):
  palavras = str.split(frase)
  list.reverse(palavras)
  espaco = " "
  x = str.lower(str.join(espaco, palavras))
  y = x.replace(".","")
  p = y.replace(",","")
  o = p.replace("!","")
  k = o.replace("?","")
  d = k.replace(":","")
  e = d.replace("-","")
  k1 = e.replace("...","")
  k2= k1.replace(";","")
  k3= k2.ljust
  return k3