def repetidos(lista_numeros):
      n=0
      rep=0
      while n<len(numeros)-1:
        if lista_numeros[n+1]==lista_numeros[n]:
             rep+=1
        n+=1
        return rep