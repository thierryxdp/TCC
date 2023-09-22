def filtraMultiplos(numero,n):
    '''Dado uma lista e um numero, a função retornará os numeros são divisiveis
       por n'''
      i=0
      lista1=[]
      while i in range(0,len(numero)):
            if numero[i]%n==0:
                  list.append(lista1,numero[i])
            i+=1
      return lista1