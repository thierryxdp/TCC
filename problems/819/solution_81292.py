def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.append(lista[i])
            
        if lista[i]==lista[-1]:
            return l
            
                

                
        i+=1