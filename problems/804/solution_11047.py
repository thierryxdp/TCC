def filtra_pares(a,b,c,d):
    
    nu1=a%2==0
    nu2=b%2==0
    nu3=c%2==0
    nu4=d%2==0
    
    if  nu1:
        tupla1= (a,)
    else:
        tupla1=( )    
    if  nu2:
        tupla2=(b,)
    else:
        tupla2=( ) 
    if  nu3:
        tupla3=(c,) 
    else:
        tupla3=( ) 
    if  nu4:
        tupla4 =(d,)
    else:
        tupla4=( ) 
        
    return (tupla1+tupla2+tupla3+tupla4)