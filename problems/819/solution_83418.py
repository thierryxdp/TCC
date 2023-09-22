def filtraMultiplos(lista,n):
    '''
       Função que retorna uma lista com os números 
       que forem divisiveis por n
     
    '''
    
    i=0
    lfinal=[]
    
    while i<len(lista):
        if lista[i] % n==0:
            lfinal.insert(i, lista[i])
            
        i+=1
            
    return lfinal