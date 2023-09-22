def lingua_p(palavra):
    """ Dado uma palavra, ela retorna na lingua do P"""
    palavra_p = ""
    vogal = 'aeiou'
    for letra in palavra:
        if vogal in palavra:
            palavra_p += 'p'
    return palavra_p