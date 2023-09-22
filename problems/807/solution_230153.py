def conta_frases(texto):
    '''Funcao que conta o numero de frases que aparece em um texto
          string -> int'''
    import re
    return len(re.split(' .| !| ? |...| ;', texto))