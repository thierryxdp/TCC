def conta_frases(frase,texto):
    '''Funcao que conta o numero de frases que aparece em um texto
          string, string -> int'''
    return len(texto.split('.', '!', '?', '...'))