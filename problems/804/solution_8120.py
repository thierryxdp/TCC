def filtra_pares(tupla):
      tupla1=tuple() 
      for i in range(len(tupla)):
           if tupla[i]%2==0:
                 tupla1+=(tupla[i],)
      return tupla1