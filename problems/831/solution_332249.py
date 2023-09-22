def lingua_p(palavra):
    '''
    Dada uma palavra, a função retorna a mesma 
    sendo que após cada vogal da palavra original, é 
    inserida a sequéncia de letras p + vogal. 
    str --> str
    '''
    palavra = list(palavra.lower())
    i = 0
    for vogal in palavra:
        if vogal in 'aáéeiúou':
            insere = 'p'+vogal
            palavra.insert(palavra.index(vogal,i)+1,insere)
        i += 1
    palavra_com_p = ''.join(palavra)
    return palavra_com_p