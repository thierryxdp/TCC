def lingua_p(palavra):
    '''
    '''
    b=''
    for i in palavra:
        if i in 'aeiou':
            a=str.replace(palavra,i, i+'p'+i)
            b=b+a
    return b