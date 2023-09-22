def maiores(lista,n):
      """Recebe uma lista de números inteiros e um número inteiro e retorna uma lista com os números maiores que N/list,int->list"""
      if type(lista)!=list or type(n)!=int:
            print("A lista deve ser do tipo list e o número deve ser inteiro")
      else:
            lista1=list()
            for i in range(len(lista)):
                  if type(lista[i])!=int:
                        print("A lista deve conter apenas números inteiros")
                        break            
                  elif lista[i]>n:
                        lista1.append(lista[i])
            lista1.sort()
            return lista1