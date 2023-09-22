def filtraMultiplos(lista,n):
    '''retorna uma nova lista com numeros divisiveis por n
    list,int->list'''
    
    i=0
    novalista=[]
    
    while i<len(lista):
        if i%n==0:
            i=i+1
            novalista=novalista+[lista[i]]
   	return novalista