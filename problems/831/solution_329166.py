def lingua_p(palavra):
    '''Traduz uma palavra(p) para a lingua do P, adiciona um p + a vogal original
    após cada vogal'''
    pt = ''
    for i in palavra:
        if palavra[i] in 'AEIOUaeiou':
            lingua = p + plavra[i]
            pt = pt + lingua
        else:
            pt = pt + palavra[i]
    return pt