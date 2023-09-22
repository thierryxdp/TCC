def filtraMultiplos(lista,num):
    filtrados=[]
    i=0
    while num*i==lista[i]:
        filtrados=filtrados+lista[i]
        i=i+1
        return filtrados