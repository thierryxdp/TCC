def filtraMultiplos(lista1,n):

    lista=[]

    i=0

    while i<len(lista1):

          if lista1[i]%n==0:

                   lista=lista+[lista1[i]]

                     i=i+1

                          return lista