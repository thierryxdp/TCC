def filtra_pares(x):
    '''função que recebe uma tuplade quatro elementos e retorna somente
    os elementos pares na ordem de inserção
    tuple->tuple'''
    
    y=()
    
    if x[0]%2==0:
        y=y+(x[0],)
    
    elif x[1]%2==0:
        y=y+(x[1],)
        
    elif x[2]%2==0:
        y=y+(x[2],)
        
    elif x[3]%2==0:
        y=y+(x[3],)
        
    return y