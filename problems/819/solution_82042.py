def filtraMultipos(lista,n,x=0):
    lista2=[]
    while x<len(lista):
        if lista[x]%n==0:
            lista2.append(lista[x])                       
        x=x+1    
    return lista2