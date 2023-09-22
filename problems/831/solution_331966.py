def lingua_p(palavra):
    '''
    '''
    for i in palavra:
        if i in 'aeiou':
            palavra.replace(i,i+'p'+i)
    return palavra