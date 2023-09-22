def media_matriz(m):
    '''
    '''
    
    soma=0
    final=0
    
    for imatriz in m:
        for i in imatriz:
            soma+=i
            final+=1
            
    M=final/soma       
            
    return M