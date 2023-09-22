def conta_numero(numero,matriz):
      """Recebe um numero inteiro e uma matriz e retorna quantas vezes o número aparece na matriz/int,list->int"""
      if type(numero)!=int:
            print("O número deve ser inteiro")
      elif type(matriz)!=list:
            print("A entrada deve ser uma lista")
      else:
            cont=0
            for i in range(len(matriz)):
                  for j in range(len(matriz)):
                        if len(matriz[i])!=len(matriz[j]):
                              print("A entrada deve ser uma matriz!")
                              cont+=1
                              break
                  if cont!=0:
                        break
      if cont==0:
            cont1=0
            for i in range(matriz):
                  for j in range(len(matriz[0])):
                        if matriz[i][j]==numero:
                              cont1+=1
            return cont1