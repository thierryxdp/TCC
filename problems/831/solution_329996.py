def lingua_p(palavra):
    """ função que retorna uma palavra em portugues para a lingua do p
    str -> str"""
    p = ''
    for i in palavra:
        if i in 'AEIOUaeiou':
            p = p + i + 'p' + i
        else:
            p = p + i
    return p