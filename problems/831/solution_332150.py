def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    palavra = ""
    vogal = 'aeiou'
    for i in palavra:
        if vogal in palavra:
            return vogal+'p'