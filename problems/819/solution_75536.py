def filtraMultiplos(lista,num):
    lista=[]
    i=0
    while i<len(lista):
        divisao=lista[i]%num
        if divisao==0:
            new=list.append(lista,lista[i])
            lista=new
        i=i+1
        return lista