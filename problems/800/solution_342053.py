def total(compras, produtos):
   '''Recebe uma lista de compras e um dicionário com os preços tabelados e
      o valor total da compra.
      list, dict -> float'''
   t = 0
   for i in range(len(compras)):
      nome = compras[i]
      if nome in produtos:
         t += produtos[nome]

   return round(t,2)