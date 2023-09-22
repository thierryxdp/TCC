def lingua_p(palavra):
    '''Traduz uma palavra para a língua do P
    str --> str'''
    palavra_p = ''
    for i in palavra.lower():
        if i in 'aáàâãeéèêiíìîoóôõuúùû':
            palavra_p += i + 'p' + i
        else:
            palavra_p += i
    return palavra_p