def filtraMultiplos(lista,num):
    new=[]
    i=1
    while i<len(lista):
        divisao=lista[i]%num
        if divisao==0:
            new=list.append(new,lista[i])
            new=new
        i=i+1
        return new