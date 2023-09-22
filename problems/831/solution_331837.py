def lingua_p(palavra):
    '''
    '''
    
    final=[]
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou' :
            final.append(palavra[i]+'p'+palavra[i])
            
            
    return final