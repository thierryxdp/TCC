def filtraMultiplos(lista,num):
    i=0
    mult=[]
    while i<len(lista):
        if lista[i]%num==0:
            mult.append(lista[i])
    	i+=1
    return mult