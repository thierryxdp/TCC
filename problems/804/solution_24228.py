def filtra_pares(x):
    '''função que recebe uma tuplade quatro elementos e retorna somente
    os elementos pares na ordem de inserção
    tuple->tuple'''
    
    y=()
    
    if x[0]%2==0:
        y=y+(x[0],)
    
    if x[1]%2==0:
        y=y+(x[1],)
        
    if x[2]%2==0:
        y=y+(x[2],)
        
    if x[3]%2==0:
        y=y+(x[3],)
        
    return y