def filtraMultiplos(lista,num):
    lista=[]
    i=0
    while i<len(lista):
        divisao=lista[i]%num
        if divisao%num==0:
            lista=list.append(lista,lista[i])
        i=i+1
        return lista