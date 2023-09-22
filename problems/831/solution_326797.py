def lingua_p(palavra):
    
    vogal = 'aeiouAEIOU'
    
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            palavra = palavra[:i+1] + 'p' + palavra[i:]
    
    return palavra