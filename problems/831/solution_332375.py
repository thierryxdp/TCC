def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    traduzida = ""
    vogal = "aeiou"
    
    for i in palavra:
        if i in vogal:
            palavra += "p"
            
    return palavra