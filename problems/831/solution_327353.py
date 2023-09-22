def lingua_p (palavraBR):
    '''Traduz a palavra recebida para a língua do P, ou seja
    após cada vogal é inserido a letra p mais a vogal original.
    string ->string'''
    frase_P = ' '
    for i in palavraBR:
        if str.lower(i) in 'aeiou':
            frase_P += i + 'p' + i
        else:
            frase_P += i
    return str.lower(frase_p)