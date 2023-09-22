def insere(lista_numero,n):
      """Recebe uma lista de números inteiros e um número e retorna a lista com esse número ordenada/list,int->list"""
      if type(lista_numero)!=list or type(n)!=int:
            print("As entradas devem ser uma lista e um número inteiro,respectivamente")
      else:
            for i in range(len(lista_numero)):
                  if type(lista_numero[i])!=int:
                        print("A lista deve ser composta por números inteiros")
                        break
            lista_numero.append(n)
            lista_numero.sort()
            return lista_numero