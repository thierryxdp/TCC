def lingua_p('palavra'):
    '''Recebe como parâmetro uma palavra(em português) e retorna esta mesma palavra traduzida para a língua do P
    str -> str'''
    newpalavra = ''
    for i in len('palavra'):
        if palavra[i] in 'AEIOUaeiou':
            newpalavra = str.replace(palavra, palavra[i], palavra[i]+'p'+palavra[i])
    return newpalavra