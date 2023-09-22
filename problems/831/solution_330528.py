def lingua_p(palavra):
    '''str-->str.'''
    list(str.lower(palavra))
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            palavra = palavra[i] + 'p' + palavra
    return palavra