def acima_da_media(numeros):
      list.sort(numeros)
      x = sum(numeros)//len(numeros)
      y =list.index(numeros,x)
      return numeros[y:]