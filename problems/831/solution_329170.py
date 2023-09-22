def lingua_p(palavra):
    '''Traduz uma palavra(p) para a lingua do P, adiciona um p + a vogal original
    após cada vogal'''
    pt = ''
    i = 0
    while i < len(palavra):
        if palavra[i] in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            lingua = palavra[i] + 'p' + palavra[i]
            pt = pt + lingua
        else:
            pt = pt + palavra[i]
        i = i + 1
    return pt