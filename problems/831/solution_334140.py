def total(compras, produtos):
  i = 0
  soma = 0
  while i < len(compras):
    if compras[i] in produtos:
      soma += produtos[compras[i]]
    i+=1
  return round(soma, 2)