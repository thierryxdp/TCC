def conta_frases(texto):
    '''Funcao que conta o numero de frases no texto colocado;
    str -> int'''

    return (len(str.split(texto, '.'))-3) + (len(str.split(texto, '?'))-1) + (len(str.split(texto, '!'))-1) + (len(str.split(texto, '...')) -1)