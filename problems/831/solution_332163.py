def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    palavra_traduzida = ""
    vogal = 'aeiou'
    for i in palavra:
        if i in palavra:
            palavra += 'p'
            
            return palavra