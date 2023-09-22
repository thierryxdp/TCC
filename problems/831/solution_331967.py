def lingua_p(palavra):
    '''
    '''
    for i in palavra:
        if i in 'aeiou':
            a=palavra.replace(i,i+'p'+i)
    return a