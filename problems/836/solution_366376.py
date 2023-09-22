def busca(setor,matriz):
      """Recebe uma matriz de 4 linhas por coluna e um setor e retorna os dados de cada funcionário do setor/str,list->list"""
      if type(setor)!=str:
            print("O elemento da busca deve ser uma string")
      elif setor.isalpha()==False:
            print("O elemento da busca deve conter apenas letras")
      elif type(matriz)!=list:
            print("A entrada deve ser uma matriz")
      else:
            cont=0
            for i in range(len(matriz)):
                  for j in range(len(matriz)):
                        if len(matriz[i])!=len(matriz[j]):
                              print("A entrada deve ser uma matriz")
                              cont+=1
                              break
                  if cont!=0:
                        break
            if cont==0:
                  cont1=0
                  for i in range(len(matriz)):
                        for j in range(len(matriz[0])):
                              if type(matriz[i][j]!=str):
                                    print("A matriz deve conter apenas strings")
                                    cont1+=1
                                    break
                        if cont1!=0:
                              break
                  if cont1==0:
                        lista=list()
                        for i in range(len(matriz)):
                              if matriz[i][2]==setor:
                                    lista.append([matriz[i]])
                        return lista