def acima_da_media(numero):
      x = sum(numeros)/len(numeros)
      list.insert(numero,0,x)
      list.sort(numero)
      y = list.index(numero,x)
      z = numero[y:]
      del z[0]
      return z