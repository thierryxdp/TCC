def lingua_p(palavra):
    '''str-->str.'''
    for i in palavra:
        if palavra[i] in 'AEIOUaeiou' == True:
            palavra = (palavra, (i+1), 'p')
        if palavra[i] in 'AEIOUaeiou' == False:
            palavra = palavra + palavra[i]    
    return str.lower(palavra)