def filtraMultiplos(lista_numeros,n):
    listanova=[]
    i=0
    while i<len(lista_numeros):
        if lista_numeros[i]%n==0:
            listanova= listanova + (lista_numeros[i],)
        i=i+1
   return listanova