def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou' :
            final+=palavra[i]+'p'+palavra[i]
            
        if palavra[i] in 'bcdfghjklmnpqrstvwxyz':
            
            final+=palavra[i]
            
    return final