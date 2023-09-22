def media_matriz(matriz):
      """Recebe uma matriz de inteiros e retorna a media de todos os números/list->float"""
      if type(matriz)!=list:
            print("A entrada deve ser uma matriz!")
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
                              if type(matriz[i][j])!=int:
                                    print("A matriz deve conter apenas números inteiros")
                                    cont1+=1
                                    break
                        if cont1!=0:
                              break
                  if cont1==0:
                        soma=0
                        for i in range(len(matriz)):
                              for j in range(len(matriz[0])):
                                  soma+=matriz[i][j]
                        media=soma/(len(matriz)*len(matriz[0]))
                        return round(media,2)