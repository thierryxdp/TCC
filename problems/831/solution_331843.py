def lingua_p(palavra):
    '''
    '''
    
    final=''
    
    for letra in range(len(palavra)):
        if letra in 'aeiou' :
            final+=letra+'p'+letra
            
            
    return final