def faltante(L):
    
    """ k """
    i=0
    a=" "
    
    
    while ( i<len(L)):
        if int(L[i])!=int(L[i-1]):
            a=a+str(int(L[i-1])+1)
        else:
            i=i+1
            
    return int(a)