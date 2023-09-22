def acima_da_media(numero):
      x = sum(numeros)/len(numeros) """Calcula a media""""
      list.insert(numero,0,x)
      list.sort(numero)
      y = list.index(numeros,x)
      z = numeros[y:]
      del z[0]
      return z