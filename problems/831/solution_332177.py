def lingua_p(palavra):
    """ Funçao que retorne uma palavra traduzida para a lingua do P"""
    
    palavra = ''
    for i in palavra:
        if i in palavra:
            palavra = str.split(palavra,'aeiou')
            return palavra