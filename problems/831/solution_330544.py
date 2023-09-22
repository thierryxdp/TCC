def lingua_p(palavra):
    '''str-->str.'''
    palavra = list(palavra)
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou' == True:
            palavra = list.insert(palavra, (i+1), 'p')
        if palavra[i] in 'aeiou' == False:
            palavra = palavra + palavra[i]    
    return str.lower(palavra)