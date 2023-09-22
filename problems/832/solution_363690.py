def eh_quadrada(m):
    '''
    '''
    
    final=0
    
    if len(m)==0:
            
        return True
    
    for i in m:
        if len(i)==len(m):
            final+=1
            
            return True
    
        else:
            return False