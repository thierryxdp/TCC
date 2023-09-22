def intercala(lista1,lista2):
      """Recebe duas listas e retorna a intercalação entre elas/list, list->list"""
      if len(lista1)>3 or len(lista2)>3:
            print("A lista deve ter apenas 3 elementos")
      else:
            for i in range(len(lista1) + len(lista2)):
                  lista3[i]=lista1[i]
                  if i+1<(len(lista1) + len(lista2)):
                        lista3[i+1]=lista2[i]
            return lista3