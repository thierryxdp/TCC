def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'abcdefghijklmnopqrstuvwxyz' :
            final+=palavra[i]+'p'+palavra[i]
            
    return final