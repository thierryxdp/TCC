def repetidos(lista_numeros):
      i=1
      rep=0
      while i<len(lista_numeros)-1:
          if lista_numeros[i]==lista_numeros[i+1]:
               rep+=1
          i+=i
          return rep