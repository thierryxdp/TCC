def faltante(lista):
     i=0
     posicao=0
     if lista[0]>1:
          return 1
     while i<len(lista):
          if ((lista[i])+1)==lista[i]:
                return lista[i+1]
          i=i+1