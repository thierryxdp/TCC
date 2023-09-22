def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.append(lista[i])
            print(i,l)
            if len(l)>0:
                return l
            i+=1
                
        i+=1