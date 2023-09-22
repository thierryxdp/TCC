def lingua_p(palavra):
    
    
    
    for vogal in palavra:
        if vogal in 'aeiou':
            vogal=vogal+'p'
        return palavra