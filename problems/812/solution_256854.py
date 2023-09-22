def retira_pontuacao(x):
  y = x.replace("."," ")
  p = y.replace(","," ")
  o = p.replace("!"," ")
  k = o.replace("?"," ")
  d = k.replace(":"," ")
  k1 = d.replace("-"," ")
  k2= k1.replace(";"," ")
  return k2