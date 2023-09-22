def filtraMultiplos(lista,n):
    counter=0
    lista2=[]
    while counter<len(lista):
        if lista[counter]%n==0:
            lista2.append(lista[counter])
        counter+=1
    return lista2