def lingua_p(palavra):
    
    palavra2=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            palavra2+=palavra[i]+'p'+palavra[i]
            
    return palavra2