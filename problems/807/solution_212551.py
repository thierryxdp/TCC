def num_frase (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''
    
    texto = texto.ljust(50, ' ')
    return texto.count('...') + texto.count(". ") + texto.count("!") + texto.count("?")