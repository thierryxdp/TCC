def filtraMultiplos(lista,n):
      """Recebe uma lista de números e um número e retorna uma lista com os números divisíveis por n"""
      if type(n)!=int and type(n)!=float:
            print("N deve ser numérico")
      else:
            for i in range(len(lista)):
                  if type(lista[i])!=int and type(lista[i])!=float:
                        print("A lista deve conter apenas números")
                        break
            lista1=list()
            for i in range(len(lista)):
                  if lista[i]%n==0:
                        lista1.append(lista[i])
            return lista1