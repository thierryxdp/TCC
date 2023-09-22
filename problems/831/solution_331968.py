def lingua_p(palavra):
    '''
    '''
    a=''
    for i in palavra:
        if i in 'aeiou':
            a=str.replace(palavra,i, i+'p'+i)
    return a