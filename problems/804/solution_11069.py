def filtra_pares(tupla):
    
    nu1=tupla[0]%2==0
    nu2=tupla[1]%2==0
    nu3=tupla[2]%2==0
    nu4=tupla[3]%2==0
    
    if  nu1:
        tupla1= (tupla[0],)
    else:
        tupla1=( )    
    if  nu2:
        tupla2=(tupla[1],)
    else:
        tupla2=( ) 
    if  nu3:
        tupla3=(tupla[2],) 
    else:
        tupla3=( ) 
    if  nu4:
        tupla4 =(tupla[3],)
    else:
        tupla4=( ) 
        
    return (tupla1+tupla2+tupla3+tupla4)