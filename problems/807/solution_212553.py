def conta_frases (texto):
    '''
    Retorna o valor de frases em
    um texto
    String -> int

    '''

    
    texto = print(texto.ljust(50))
    return texto.count('...') + texto.count(". ") + texto.count("!") + texto.count("?")