def inverte(f):
    '''
    A função retorna uma frase com as
    palavras na ordem inversa
    (entrada = str / saída = str)
    '''
    f = str.replace(f, '...', '[]')
    f = str.replace(f, '[]', '')
    f = str.replace(f, '.', '')
    f = str.replace(f, '!', '')
    f = str.replace(f, '?', '')
    f = str.replace(f, ',', '')
    f = str.replace(f, ';', '')
    f = str.replace(f, ':', '')
    return str.join(list.reverse(str.split(f)))