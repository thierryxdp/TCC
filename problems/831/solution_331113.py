def lingua_p(palavra):
    '''recebe uma palavra e a traduz para a lingua do P
    str->str'''
    str.lower(palavra)
    tradu = ''
    for i in palavra:
        tradu = tradu + i
        if i in 'aeiouáéíóú':
            tradu = tradu + 'p' + i
    return tradu