def filtraMultiplos(lista,num):
    lista=[]
    i=0
    while i<len(lista):
        if lista[i]%num==0:
        	lista=lista+(lista[i])
    i=i+1
    return lista