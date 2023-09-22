def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou' :
            final+=palavra[i]+'p'+palavra[i]
            
    return palavra.join(final)