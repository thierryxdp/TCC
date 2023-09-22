def repetidos(numeros):
      n=0
      soma=0
      while n<len(numeros)-1:
        if numeros[n+1]==numeros[n]:
             soma+=1
        n+=1
        return soma