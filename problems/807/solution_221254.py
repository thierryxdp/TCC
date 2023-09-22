def conta_frases (frases):
    '''Conta o número de frases em um texto. Toda frase termina
    com ponto final, de exclamação, interrogação, ou reticências.
    A função então troca toda exclamação, interrogação e 
    reticências por ponto final atraves de str.replace(), para
    poder então contar o número de pontos finais com str.count().
    str >> int
    '''
    
    frases = str.replace(frases,'?','.')
    frases = str.replace(frases,'!','.')
    frases = str.replace(frases,'...','.')
    numero = str.count(frases,'.')
    return (numero)