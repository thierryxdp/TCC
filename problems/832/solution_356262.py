def eh_quadrada(matriz):
      """Recebe uma matriz e retorna True se for quadrada ou False senão for/list->bool"""
      cont=0
      if type(matriz)!=list:
            print("A entrada deve ser uma lista")
      else:
            for i in range(len(matriz)):
                  for j in range(len(matriz)):
                        if len(matriz[i])!=len(matriz[j]):
                              print("A entrada deve ser uma matriz!")
                              cont+=1
                              break
                  if cont!=0:
                        break
            if cont==0:
                  if len(matriz)==0:
                        return True
                  elif len(matriz)==len(matriz[0]):
                        return True
                  else:
                        return False