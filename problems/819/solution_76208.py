def filtraMultiplos(lista,n):
    i= 0
    total=len(lista)-1
    x=[]
    while i < total:
       print(i)
       i=i+1
       if lista[i]%n == 0:
         print('entrei aq')
         p= x.append(lista[i])
    return p