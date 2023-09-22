def conta_frases (frases):
    """retorna o número de frases que aparecem no texto. Cada frase
termina com um ponto final, exclamação, interrogação ou três pontos.
str -> int"""
    '...' != '.'
    frases2 = str.replace(frases,'...','*',99)
    if '.' in frases2:
        str.count(frases,'.')
    elif '!' in frases2:
        str.count (frases2,'!')
    elif '?' in frases2:
        str.count(frases2,'?')
    return str.count(frases2,'.') + str.count(frases2,'*') + str.count (frases2,'!') + str.count(frases2,'?')