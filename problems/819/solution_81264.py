def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l+=lista[i]
            if i==len(lista):
                return l
       
    	i+=1