def filtraMultiplos(lista,n):
    '''retorna uma nova lista com numeros divisiveis por n
    list,int->list'''
    
    i=0
    novalista=[]
    
    while i<len(lista):
        if lista[i]%n==0:
    	    list.append(novalista,lista[i])
        i=i+1
   	
    return novalista