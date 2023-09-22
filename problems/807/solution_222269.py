def conta_frases (frases):
    """retorna o número de frases que aparecem no texto. Cada frase
termina com um ponto final, exclamação, interrogação ou três pontos.
str -> int"""
    frases1 = str.replace(frases,'...','#',100)
    if '.' in frases1:
        str.count(frases1,'.')
        
    elif '!' in frases1:
        str.count (frases1,'!')
        
    elif '?' in frases1:
        str.count(frases1,'?')
    return str.count(frases1,'.') + str.count(frases1,'#') + str.count (frases1,'!') + str.count(frases1,'?')