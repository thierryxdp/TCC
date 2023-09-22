def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    traduzida = palavra[:]
    vogal = "aeiou"
    
    for i in palavra:
        if i in vogal:
            traduzida = palavra + "p"
            
    return traduzida