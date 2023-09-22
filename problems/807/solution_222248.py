def conta_frases (frases):
    """retorna o número de frases que aparecem no texto. Cada frase
termina com um ponto final, exclamação, interrogação ou três pontos.
str -> int"""
    '...' != '.'
    if '.' in frases:
        str.count(frases,'.')
    elif '...' in frases:
        str.replace(frases,'...', @)
        str.count(frases,@)
    elif '!' in frases:
        str.count (frases,'!')
    elif '?' in frases:
        str.count(frases,'?')
    return str.count(frases,'.') + str.count(frases,'...') + str.count (frases,'!') + str.count(frases,'?')