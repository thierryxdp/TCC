def filtraMultiplos(lista,n):
    i=0
    listaNova=[]
    
    while i < len(lista):
        if lista[i]%n==0:
            list.append(listaNova,lista[i])
        i=i+1
    return listaNova