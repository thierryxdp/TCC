def lingua_p(palavra):
    '''Traduz a palavra inserida
    para a lingua p
    str --> str'''
    palavra = str.lower(palavra)
    p = ''
    for i in palavra:
        if i in 'aeiouãõáéíóú':
            p = p + i + 'p' + i
        else :
            p = p + i
    return p