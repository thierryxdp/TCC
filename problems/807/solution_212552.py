def num_frase (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''
    
    
    return texto.count('...') + texto.count(". ") + texto.count("!") + texto.count("?")