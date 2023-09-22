def acima_da_media(lista):
      """Recebe uma lista de notas e retorna uma lista com as notas acima da media/list->list"""
      k=0
      soma=0
      lista1=list()
      for i in range(len(lista)):
            if type(lista[i])!=int and type(lista[i])!=float:
                  k+=1
                  print("A lista deve conter números")
                  break
            elif i<len(lista):
                  soma+=lista[i]
            else:
                  media=soma/len(lista)
                  for j in range(len(lista)):
                        if lista[j]>media:
                              lista1.append(lista[j])
      if k==0:
            lista1.sort()
            return lista1