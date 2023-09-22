def faltante(L):
    
    """ Descobre qual número inteiro da lista L está faltando. Lista--> int """
    i=0

    
    
    while ( i<len(L)):
        if i+1 not in L:
            return i+1
        i=i+1
      
          
            
    return i+1