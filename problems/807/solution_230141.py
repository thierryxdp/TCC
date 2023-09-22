def conta_frases(texto):
    '''Funcao que conta o numero de frases que aparece em um texto
          string, string -> int'''
    return str.count(str.split(texto, '.' '!' '?' '...' ';'))