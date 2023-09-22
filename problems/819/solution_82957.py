def filtraMultiplos(lista, n):
    ''' '''
    filtrado=[]
    i=0
    while i < len(lista):
        if lista[i]%n==0:
            list.append(lista[i])
        i+=1           
    
    return filtrado