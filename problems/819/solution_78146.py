def filtraMultiplos(lista,n):
    multiplo=[]
    i=0
    
    while i < len(lista):
        if lista[i]%n==0:
            multiplo=multiplo+[lista[i]]
        i=i+1
    return multiplo