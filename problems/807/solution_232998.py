def conta_frases (frases):
    '''Recebe um pequeno texto e retorna o número de frases contidas 
    nele. O critério é que pontos finais, pontos de exclamação, pontos
    de interrogação e três pontos denotarão o fim da frase'''
    n1 = str.count(.) in (frases)
    n2 = str.count(!) in (frases)
    n3 = str.count(?) in (frases)
    n4 = str.count(...) in (frases)
    return n1 + n2 + n3 + n4