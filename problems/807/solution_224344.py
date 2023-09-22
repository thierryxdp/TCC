# A função recebe um texto e conta o número de frases que aparecem neste texto. Cada frase no texto
# é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos
# em sequência (reticências).
# string->int

def conta_frases(texto):
    texto = str.replace(texto,'...','.')
    texto = list(texto)
    numero_frases = list.count(texto,'.') + list.count(texto,'!') + list.count(texto,'?')
    return numero_frases