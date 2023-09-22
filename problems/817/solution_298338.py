def acima_da_media(numero):
      x = sum(numero)/len(numero)
      list.insert(numero,0,x)
      list.sort(numero)
      y = list.index(numero,x)
      if y in not numero:
            return numero[y+1:]
      else:
            return teste