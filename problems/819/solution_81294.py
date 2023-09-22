def filtraMultiplos(lista,n):
    "Filtre a lista dada para multiplos inteiros de n; lista,int->lista"
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.append(lista[i])
            
        
               
        i+=1
     return l