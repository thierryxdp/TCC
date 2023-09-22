def filtraMultiplos(lista,n):
    result=0
    listafinal=[]
    while result<len(lista):
        if lista[result]%n==0:
            listafinal=listafinal+[lista[result]]
        result+=1
    return listafinal