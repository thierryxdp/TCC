def faltante(lista):
      """Recebe uma lista de números inteiros e retorna o número faltante"""
      x=0
      for i in range(len(lista)):
            if type(lista[i])!=int:
                  x+=1
                  print("A lista deve conter apenas números inteiros")
                  break
      if x==0:
            lista.sort()
            for i in range(len(lista)):
               if lista[i]!=i+1:
                     return i+1
               elif i==len(lista)-1:
                     return len(lista)+1