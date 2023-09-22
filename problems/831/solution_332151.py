def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    palavra_p = ""
    vogal = 'aeiou'
    for letra in palavra:
        if letra in vogal:
            palavra_p = palavra_p + 'p'
        else:
            palavra_p = palavra_p + letra
    return