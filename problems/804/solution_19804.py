def filtra_pares (a):
    '''
    (2,5,6,7) --> (2,6) 
    '''  
    if a[0]%2==0:
        tupla0=(a[0],)
    else:
        tupla0=()
    if a[1]%2==0:
        tupla1=(a[1],)
    else:
        tupla1=()
    if a[2]%2==0:
        tupla2=(a[2],)
    else:
        tupla2=()
    if a[3]%2==0:
        tupla3=(a[3],)
    else:
        tupla3=()
        
    return (tupla0+tupla1+tupla2+tupla3)