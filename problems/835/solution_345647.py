def melhor_volta(matriz):
      """Recebe uma matriz 6x10 e retorna uma tupla com os dados/list->tuple"""
      if type(matriz)!=list:
            print("A entrada deve ser uma matriz!")
      elif len(matriz)!=6 or len(matriz[0])!=10:
            print("A matriz deve ser 6x10!")
      else:
            cont=0
            for i in range(len(matriz)):
                  for j in range(len(matriz[0])):
                        if type(matriz[i][j])!=int and type(matriz[i][j])!=float:
                              print("A matriz deve conter dados numéricos")
                              cont+=1
                              break
                  if cont!=0:
                        break
            if cont==0:
                  lista=list()
                  for i in range(len(matriz)):
                        x=min(matriz[i])
                        y=matriz[i].index(x)
                        lista.append([x,y])
                  for i in range(len(lista)):
                        for j in range(len(lista)):
                              if lista[i][0]<lista[j][0]:
                                    z=lista[i][0]
                                    w=i
                                    v=lista[i][1]
                  tupla=(w+1,z,v+1)
                  return tupla