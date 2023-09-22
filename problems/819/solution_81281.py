def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.append(lista[i])
            
            if i+1==len(lista):
                return l
                
        i+=1