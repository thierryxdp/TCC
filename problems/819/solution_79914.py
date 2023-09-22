def filtraMultiplos(lista,n):

    listafinal = []

    k = 0
    
    while k<len(lista):

        if lista[k]%n==0:

            listafinal = listafinal + [lista[k]]
        
        k = k +1
    
    return listafinal