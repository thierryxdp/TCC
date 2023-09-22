def conta_frases (frases):
    '''Recebe um pequeno texto e retorna o número de frases contidas 
    nele. O critério é que pontos finais, pontos de exclamação, pontos
    de interrogação e três pontos denotarão o fim da frase'''
    n1 = frases.count(".") 
    n2 = frases.count("!") 
    n3 = frases.count("?") 
    n4 = frases.count("...") 
    return n1 + n2 + n3 + n4