def filtraMultiplos(numero,n):
      '''Dado uma lista e um numero, a função retornará os numeros são divisiveis
       por n'''
      list.sort(numero)
      i=0
      lista1=[]
      while i <= len(numero)-1:
            print(numero[i])
            if numero[i]%n==0:
                  list.append(lista1,numero[i])
            i+=1
      return lista1