def acima_da_media(numero):
      x = sum(numero)/len(numero)
      list.insert(numero,0,x)
      list.sort(numero)
      y = list.index(numero,x)
      return y