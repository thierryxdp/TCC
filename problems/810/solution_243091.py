def inverte(f):
    '''
    A função retorna uma frase com as palvras
    na ordem inversa
    (entrada = str / saída = str)
    '''
    f = str.replace(f, '...', '[]')
    f = str.replace(f, '.', ' ')
    f = str.replace(f, ';', ' ')
    f = str.replace(f, ',', ' ')
    f = str.replace(f, ':', ' ')
    f = str.replace(f, '-', ' ')
    f = str.replace(f, '?', ' ')
    f = str.replace(f, '!', ' ')
    f = str.replace(f, '[]', ' ')
    f = str.split(str.lower(f))
    list.reverse(f)
    return str.join(' ', f)