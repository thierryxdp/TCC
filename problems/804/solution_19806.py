def filtra_pares (a):
    '''
    função que recebe uma tupla com quatro elementos inteiros
    como parametro e retorna uma nova tupla contendo apenas os 
    elementos pares.
    tupla-> tupla
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