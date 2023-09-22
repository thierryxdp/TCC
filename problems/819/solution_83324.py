def filtraMultiplos(lista,n):
    '''
    '''
    
    
    i=0
    lfinal=[]
    while len(lista)//n:
        
        if lista[i]%2==0:
            
            lfinal+=[lista[i]]
        
        i+=1
           
    return lfinal