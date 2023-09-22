def lingua_p(palavra):
    
    palavra2=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            str.strip(palavra,palavra[i])
            palavra2+=palavra2+'p'
            
    return palavra2