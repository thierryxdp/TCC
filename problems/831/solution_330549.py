def lingua_p(palavra):
    '''str-->str.'''
    for i in palavra:
        if palavra[i] in 'AEIOUaeiou':
            palavra = (palavra, (i+1), 'p')
        if palavra[i] not in 'AEIOUaeiou':
            palavra = palavra + palavra[i]    
    return str.lower(palavra)