def filtraMultiplos(lista,n):
    "Filtre os multiplos de um numero n de uma dada lista; lista, int->lista"
    l=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            l.append(lista[i])
            if i+1==len(lista):
                return l
            
            
            
        i+=1