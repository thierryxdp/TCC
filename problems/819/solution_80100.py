def filtraMultiplos(lista,num):
    filtrados=[]
    i=0
    while i<len(lista):
        if lista[i]%num==0:
        	filtrados=filtrados+[lista[i]]
        i=i+1
    return filtrados