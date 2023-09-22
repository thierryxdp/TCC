def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    palavra_trad = ""
    
    for letra in palavra:
        if letra == 'aeiou':
            palavra_trad = palavra_trad + "p"
            return palavra_trad