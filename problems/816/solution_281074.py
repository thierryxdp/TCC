def maiores(lista,n):
    novalista=[]
    while lista[len(lista)-1]>=0:
        if lista(len(lista)-1)>n:
            novalista=novalista+lista(len(lista)-1)
        len(lista)=len(lista)-1
    return list.sort(novalista)