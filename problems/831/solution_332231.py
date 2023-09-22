def lingua_p(palavra):
    '''
    
    '''
     palavra = list(palavra.lower())
    i = 0
    for vogal in palavra:
        if vogal in 'aeiou':
            insere = 'p'+ vogal
            palavra.insert(palavra.index(vogal,i)+1,insere)
        i += 1
    x = ''.join(palavra)
    return x