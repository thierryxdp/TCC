def lingua_p(palavra):
    '''
    '''
    
    for i in palavra:
        if i in 'aeiou':
            a= i+'p'+i
            palavra=palavra+a
    return palavra