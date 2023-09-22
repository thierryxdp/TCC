def lingua_p(palavra):
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            str.replace(palavra,palavra[i],palavra[i]'p')
    return palavra