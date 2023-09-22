def filtraMultiplos(lista,n):
    i= 0
    total=len(lista)-1
    x=[]
    while i < total:
       i=i+1
       if lista[i]%n == 0:
         print(lista[i])
         p= x.append(lista[i])
    return p