def filtraMultiplos(numero,n):
      list.sort(numero)
      i=0
      lista1=[]
      while i in range(0,len(numero)):
            print(numero[i])
            if numero[i]%n==0:
                  list.append(lista1,numero[i])
            i+=1
      return lista1