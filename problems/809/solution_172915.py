def intercala(lista1,lista2):
      """Recebe duas listas e retorna a intercalação entre elas/list, list->list"""
      if type(lista1)!=list or type(lista2)!=list:
            print("Os dados devem ser uma lista")
      elif len(lista1)>3 or len(lista2)>3:
            print("A lista deve ter apenas 3 elementos")
      else:
            lista3=[]
            for i in range(len(lista1)):
                  lista3.append(lista1[i])
                  lista3.append(lista2[i])
            return lista3