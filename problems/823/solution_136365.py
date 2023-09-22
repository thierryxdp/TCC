def faltante(valor):
      list.sort(valor)
      if 1 not in valor:
            return 1
      elif valor[-1] < len(valor) + 1:
            return len(valor) + 1
      i = 0
      x = 0
      while i < len(valor) - 1:
            if valor[i + 1] - valor[i] > 1:
                  x = x + valor[i] + 1
            i = i + 1
      return x