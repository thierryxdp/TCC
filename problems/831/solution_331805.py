def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou' :
            final+=letra+'p'+letra
            
    return final