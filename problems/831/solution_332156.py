def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    palavra_traduzida = ""
    vogal = 'aeiou'
    for i in palavra:
        if vogal in palavra:
            palavra_traduzida = str.join('p',palavra)
            return palavra_traduzida