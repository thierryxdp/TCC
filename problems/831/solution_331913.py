def lingua_p(palavra):
    
    palavra2=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáé':
            palavra2+=palavra[i]+'p'+palavra[i]
            
        else:
            palavra2+=palavra[i]
            
    return palavra2