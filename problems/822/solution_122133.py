def repetidos(lista):
      """Recebe uma lista de números e retorna a quantidade de vezes que o elemento da lista é igual o anterior"""
      x=0
      for i in range(len(lista)):
            if type(lista[i])!=int and type(lista[i])!=float:
                  x+=1
                  print("A lista deve conter apenas números")
                  break
      y=0
      if x==0:
            for i in range(len(lista)):
                  if lista[i]==lista[i-1]:
                      y+=1
            return y