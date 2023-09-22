def filtraMultiplos(lista,n):
    l=[]
    i=0
    while i<len(lista):
        while lista[i]%n==0:
            l=l+[lista[i]]                                                                      
        i=i+1